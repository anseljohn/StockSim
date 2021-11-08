from Stock import Stock

if __name__ == "__main__":
    random = Stock("AAPL")
    print(random.profit())
    print(random.current())
    print(random.ticker)

    while True:
        print("\r", random.current(), end="")
