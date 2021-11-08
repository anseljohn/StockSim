from Stock import Stock
from Portfolio import Portfolio

if __name__ == "__main__":
    me = Portfolio("anseljohn", 100000)
    me.buy_stock("AAPL", 10)
    me.buy_stock("AMZN", 10)
    print(me)
