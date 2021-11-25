import math
import yfinance as yf
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

df = yf.download('aapl', period="1d", interval="1m")
df['4avg'] = df[['Open','Close','High','Low']].mean(axis=1)
df['hl_avg'] = df[['High','Low']].mean(axis=1)
print(df)

avgplt = plt.figure(1)
openplt = plt.figure(2)

df['4avg'].plot(label='avg', c='red', alpha=.150, lw=1)
df['hl_avg'].plot(label='aapl', c='green', alpha=.150, lw=1)
plt.title("Open")
plt.show()

print(df.columns)
