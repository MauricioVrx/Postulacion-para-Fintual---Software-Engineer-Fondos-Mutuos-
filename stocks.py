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
        # the Portfolio class has a collection of “allocated” Stocks
        self.stocks   = {} # Diccionario de acciones disponibles
        self.holdings = {} # Cantidad de cada acción en el portafolio

    def add_stock(self, stock):
        pass

    def rebalance(self):
        pass
    