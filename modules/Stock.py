from yahoo_fin import stock_info as si

class Stock:

    def __init__(self, ticker, count):
        self.ticker = ticker
        self.initPrice = si.get_live_price(ticker)
        self.count = count

    def profit(self):
        return count * (si.get_live_price(self.ticker) - self.initPrice)

    def current(self):
        return si.get_live_price(self.ticker)

    def total(self):
        return self.current() * self.count
