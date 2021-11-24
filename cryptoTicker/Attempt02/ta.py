import numpy
import talib
from numpy import genfromtxt

# close = numpy.random.random(100)

my_data = genfromtxt('15minutes.csv', delimiter=',')

print(my_data)
close = my_data[:,4] # gets the 4th item in the array in csv file
# print(close)

# moving_average = talib.SMA(close)
rsi = talib.RSI(close)

# print(moving_average)
print(rsi)
