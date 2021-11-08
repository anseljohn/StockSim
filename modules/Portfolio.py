import yfinance as yf

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock):
        self.stocks.update({stock.ticker: stock})

    def stock_profit(self, ticker):
        return self.stocks.get(ticker).profit()

    def profits(self):
        profits = 0

        for ticker in self.stocks:
            profits += self.stocks.get(ticker).profit()

        return profits

    def value_owned(self):
        val_owned = 0

        for ticker in self.stocks:
            val_owned += self.stocks.get(ticker).current()

        return val_owned

