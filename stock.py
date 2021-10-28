class Stock():
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol

    def get_previous_closing_price(self):
        return self.__previousClosingPrice

    def set_previous_closing_price(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice

    def get_current_price(self):
        return self.__currentPrice

    def set_current_price(self, currentPrice):
        self.__currentPrice = currentPrice

    def get_change_percent(self):
        return self.__previousClosingPrice - self.__currentPrice / self.__previousClosingPrice * 100



