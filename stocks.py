class Stock:
    # Construct a simple Portfolio class that has a collection of Stocks. Assume each Stock has a “Current Price” method that receives the last available price.
    """
    Representa una acción que contendrá el símbolo de identificación junto al precio actualizado.

    Args:
        symbol (str): Símbolo de la acción
        price (float): Precio actual de la acción
    """
    def __init__(self, symbol, price):
        self.symbol = symbol  # Símbolo de las acción
        self.price = price   # Precio interno

    def __str__(self):
        return f'{self.symbol} / {self.price}'

    def current_price(self):
        """ Función que retorna el valor actual de la acción. """
        return self.price

    def update_price(self, new_price):
        """ Función que permite actualizar el precio de la acción """
        self.price = new_price


class Portfolio:
    def __init__(self):
        self._stocks   = {} # Diccionario de acciones disponibles
        self._holdings = {} # Cantidad de cada acción en el portafolio

    def add_stock(self, stock, holding = 0):
        """Añade una acción al conjunto disponible"""
        self._stocks[stock.symbol] = stock
        self._holdings[stock.symbol] = holding

    def get_total_value(self):
        total = 0.0
        for symbol, quantity in self._holdings.items():
            total += self._stocks[symbol].current_price() * quantity 
        return total
    
    def exist_stock(self, symbol):
        if symbol in self._holdings:
            return True
        else:
            return False
    
    def set_holding(self, symbol, quantity):
        if self.exist_stock(symbol):
            self._holdings[symbol] = quantity
            print(f'La acción "{symbol}" dispone de {quantity} unidades')
        else:
            print(f'No existe stock con nombre "{symbol}"')

    def comprobate_allocation(self, allocation_dict, error_margin = 0.01):
        """Establece la distribución objetivo de acciones"""
        # Verificar que la suma sea ≈ 100%
        total = sum(allocation_dict.values())
        if abs(total - 1.0) > error_margin:  # Permite pequeño margen de error
            return False
        return True


    def rebalance(self, allocation_dict):
        if self.comprobate_allocation(allocation_dict) == False:
            raise ValueError("La asignación debe sumar 100%")
        
        # 1. Validar los nombres de la distribución frente al listado de stock en el portafolio
        for stk in allocation_dict:
            # print(stk)
            if not self.exist_stock(stk):
                print('No existe la acción: {stk}')
                break

        # 1. Calcular valor total del portafolio
        current_total_value = self.get_total_value()

        print()
        print(f'Precio total actual: {current_total_value}')
        # for st, i in self._holdings.items():
        #     print(f'{st}: {i}  *  {self._stocks[st].price} = {i*self._stocks[st].price}')
        
        
        # print()
        # for st, i in allocation_dict.items():
        #     stock_price = self._stocks[st].price
        #     print(f'{st}: {i} // {stock_price} || stk = {self._holdings[st]}')
        #     sub_total = (total_value/stock_price)*i-self._holdings[st]
        #     print(f'{sub_total}')
        #     print(f'{sub_total*stock_price}')
        #     if sub_total < 0:
        #         print(f'Vender: {abs(sub_total)} acciones de "{st}"')
        #     elif sub_total > 0:
        #         print(f'Comprar: {abs(sub_total)} acciones de "{st}"')
        #     print()

        for st in self._holdings:
            if st not in allocation_dict:
                if self._holdings[st] > 0:
                    print(f'VENDER - {self._holdings[st]}')
                else:
                    continue
            else:
                print(allocation_dict[st])
                stock_price = self._stocks[st].price
                porcentual_allocation_dict = allocation_dict[st]


                sub_total = (current_total_value/stock_price)*porcentual_allocation_dict - self._holdings[st]


                if sub_total < 0:
                    print(f'VENDER: {abs(sub_total)} acciones de "{st}"')
                elif sub_total > 0:
                    print(f'COMPRAR: {abs(sub_total)} acciones de "{st}"')

            print()





meta = Stock("META", 485.75)
aapl = Stock("AAPL", 172.35)
ntvr = Stock("NTVR", 262.35)
msft = Stock("MSFT", 407.54)

stc = Portfolio()
stc.add_stock(meta)
stc.add_stock(aapl)
stc.add_stock(ntvr)
stc.add_stock(msft,2)

stc.set_holding('META',2)

# stc._stocks
# stc._holdings
# stc.get_total_value()
allo = {"META":0.4, "AAPL":0.6}
# stc.comprobate_allocation({"META":0.4, "AAPL":0.6})
stc.rebalance(allo)