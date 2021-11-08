import yfinance as yf
from Stock import Stock
from utils import *

class Portfolio:
    def __init__(self, user, init_balance):
        self.user = user
        self.stocks = {}
        self.balance = init_balance

    def buy_stock(self, ticker, count):
        to_add = Stock(ticker, count)
        self.balance -= to_add.total()
        self.stocks.update({ticker:to_add})

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
            val_owned += self.stocks.get(ticker).total()
        return val_owned

    def print_value_owned(self):
        return self.user + "'s owned value: $" + format(self.value_owned(), '.2f')


    def __str__(self):
        string = "\n" + self.user + "'s portfolio:\n\t"
        string += "Total profit: " + pmoney(self.profits()) + "\n\t"
        string += "Total value: " + pmoney(self.value_owned()) + "\n\t"
        string += "Amt uninvested: " + pmoney(self.balance) + "\n\n\t"

        for ticker in self.stocks:
            string += str(self.stocks.get(ticker)) + "\n\t"

        return string

