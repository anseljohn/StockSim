import yfinance as yf
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

hist = yf.download('aapl',period="1d",interval="1m")
print(hist.values)
hist['Open'].plot(label="aapl")
plt.title("AAPL over time: 1d, 1m inc")
plt.show()
