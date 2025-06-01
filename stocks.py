class Stock:
    """
    Representa una acción que contendrá el símbolo de identificación junto al precio actualizado.

    Args:
        symbol (str): Símbolo de la acción
        price (float): Precio actual de la acción
    """
    def __init__(self, symbol, price):
        self.symbol = symbol  # Símbolo de las acción
        self._price = price   # Precio interno

    def __str__(self):
        return f'{self.symbol} / {self._price}'

    def current_price(self):
        """ Retorna el valor actual de la acción."""
        return self._price

    def update_price(self, new_price):
        """ Permite actualizar el precio de la acción """
        self._price = new_price


class Portfolio:
    def __init__(self):
        self._stocks   = {} # Diccionario de acciones disponibles
        self._holdings = {} # Cantidad de cada acción en el portafolio

    def add_stock(self, stock, holding = 0):
        """Añade una acción al conjunto disponible"""
        self._stocks[stock.symbol]   = stock
        self._holdings[stock.symbol] = holding

    def get_total_value(self):
        """Función que retorna la suma el valor y cantidad de acciones que tiene el portafolio."""
        total = 0.0
        for symbol, quantity in self._holdings.items():
            total += self._stocks[symbol].current_price() * quantity 
        return total
    
    def stock_exists(self, symbol):
        """Función que permite validad si una acción existe en el portafolio."""
        if symbol in self._holdings:
            return True
        else:
            return False
    
    def update_holding_quantity(self, symbol, quantity):
        """Asigna la cantidad de una misma accion de un portafolio."""
        if self.stock_exists(symbol):
            self._holdings[symbol] = quantity
        else:
            print(f'Acción "{symbol}" no existe en el portafolio')

    def check_percentage_allocation(self, allocation_dict, error_margin = 0.01):
        """Comprueba la distribución objetivo de acciones, este debe tener una suma que sea ≈ 100%(Opcional: Con un margen de error)."""
        total = sum(allocation_dict.values())
        if abs(total - 1.0) > error_margin:  # Permite pequeño margen de error
            return False
        return True
    
    def _make_holding_transaction(self, transaction_list):
        """Al realizar los calculos de de compra-venta de acciones se realizan los cambios al diccionario "self._holdings" con el valor actuaal junto al valor a sumar o restar."""
        for transaction in transaction_list:
            transaction_value = transaction[2]
            if transaction[1] == 'SELL': # En caso sea venta el valor a modificar se cambia a negativo
                transaction_value *= -1
            current_holding = self._holdings[transaction[0]]
            self.update_holding_quantity(transaction[0], current_holding+transaction_value)
 
    def rebalance(self, allocation_dict):
        """
        Función que permite calcular las transacciones necesarias para alcanzar la distribución objetivo.

        Args:
            allocation_dict (dict): Diccionario con el nombre de la accion con el porcentaje en forma de decimal. (Ejemplo: {"META":0.4, "AAPL":0.6})

        Return:
            list: Transacciones como tupas (símbolo, acción, cantidad)
                acciones: 'BUY'(Comprar) o 'SELL'(Vender)
        """
        # 1. Validar el valor porcentual de allocation_dict sea coorespondiente ≈ 100%
        if self.check_percentage_allocation(allocation_dict) == False:
            raise ValueError("La asignación porcentual debe sumar ≈100%")
        
        # 2. Validar si los nombres de la distribución existen en el listado de stock del portafolio
        missing_stocks = [stock for stock in allocation_dict if not self.stock_exists(stock)]  
    
        if missing_stocks:
            raise ValueError(f"Acciones no existentes: {', '.join(missing_stocks)}")

        # 3. Obtener datos necesarios y creación de lista que almacenará las transacciones a realziar 
        current_total_value = self.get_total_value() # Calcular valor actual 
        transactions = [] # 

        # 4. Calcular valor total del portafolio
        for symbol, quantity in self._holdings.items():
            if symbol not in allocation_dict:
                # En caso de que la acción del portafolio NO EXISTA en el nuevo listado, se venderán('SELL') todas las unidades del mismo y se agregará el resultado a lista de "transactions".
                if self._holdings[symbol] > 0:
                    transactions.append((symbol, 'SELL', quantity))
                else:
                    continue
            else:
                # En caso de EXISTA se relizará el calculo correspondiente
                stock_price = self._stocks[symbol]._price
                porcentual_allocation_dict = allocation_dict[symbol]

                result = (current_total_value/stock_price)*porcentual_allocation_dict - quantity

                # Si el valor es positivo será 'BUY'(compra), en caso de que sea menor será 'SELL'(venta)y se agregará el resultado a lista de "transactions".
                if result < 0:
                    transactions.append((symbol, 'SELL', abs(result)))
                elif result > 0:
                    transactions.append((symbol, 'BUY', abs(result)))
        
        # Cuando se realizan todas las operaciones de manera exitosa, se procede a modificar la cantidad de acciones en el portafolio
        self._make_holding_transaction(transactions)
        return transactions

