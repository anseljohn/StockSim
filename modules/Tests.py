from Stock import Stock
from Portfolio import Portfolio

if __name__ == "__main__":
    me = Portfolio("anseljohn", 2500)
    me.buy_stock("AAPL", 10)
    print(me.value_owned())
