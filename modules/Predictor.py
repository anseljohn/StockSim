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

avgplt = plt.figure(1)
openplt = plt.figure(2)

df['4avg'].plot(label='avg', c='red', alpha=.150, lw=1)
df['hl_avg'].plot(label='aapl', c='green', alpha=.150, lw=1)

for name in df.columns:
  if name != '4avg' and name != 'hl_avg':
    del df[name]


plt.title("Averages")
plt.show()

# Use (0): OHCL avg or (1): HL avg
avg = 1
del df['4avg' if avg != 0 else 'hl_avg']

# Fixed seed
np.random.seed(7)

# Fit to 0-1
scaler = MinMaxScaler(feature_range=(0, 1))

ds = df.values.astype("float32")
ds = scaler.fit_transform(ds)

# Separate training and testing data
train_sz = int(len(ds) * 0.67)
test_sz = len(ds) - train_sz
train, test = ds[0:train_sz,:], ds[train_sz:len(ds),:]

# Data set as x->x1, x1->x2, ... xn-1->xn
def mkds(ds, lookback=1):
  dx, dy = [], []
  for i in range(len(ds) - lookback - 1):
    a = ds[i:(i+lookback)]
    dx.append(a)
    dy.append(ds[i+lookback])
  return np.array(dx), np.array(dy)

trainX, trainY = mkds(train)
testX, testY = mkds(test)

# reshape into X=t and Y=t+1
look_back = 1
trainX, trainY = mkds(train, look_back)
testX, testY = mkds(test, look_back)
# reshape input to be [samples, time steps, features]
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
# create and fit the LSTM network
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)
# make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)
# invert predictions
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform(trainY)
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform(testY)
# calculate root mean squared error
trainScore = math.sqrt(mean_squared_error(trainY, trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY, testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))
# shift train predictions for plotting
trainPredictPlot = np.empty_like(ds)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
# shift test predictions for plotting
testPredictPlot = np.empty_like(ds)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(ds)-1, :] = testPredict
# plot baseline and predictions
plt.plot(scaler.inverse_transform(ds))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()
