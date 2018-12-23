import numpy as np
import scipy as sc
# count : len()
# average, mean
# varience, std
# max, min, median
# quartile, percentile

# x = {1,2,3,...,n} ==> x = np.array([1,2,3,...,n])
x = np.array([1,2,3,4,5])
print(len(x))
print(np.average(x))
print(np.var(x))
print(np.std(x))
print(np.quantile(x,0.5))
print(np.median(x))

y = np.arange(100)
print(np.quantile(y, 0.5))  # 49.5
print(np.median(y))         # 49.5
print(len(y))               # 100
print(np.percentile(y, 0))  # 0.0   : 최소값
print(np.percentile(y, 24)) # 23.76 : 1사분위수