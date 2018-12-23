import numpy as np
import matplotlib.pylab as plt

# normal distribution
m, sigma = 0, 0.1
s = np.random.normal(m,sigma,1000)
count,bins,patches = plt.hist(s,30,normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(bins-m)**2/(2*sigma**2)), linewidth=2, color='r')
plt.show()

# scatter
# 두 개의 실수 데이터 집합의 상관관계를 살펴볼 때 이요

# np.random.normal(avg, std, sample size)
X = np.random.normal(0,1,100)
Y = np.random.normal(0,1,100)

plt.scatter(X,Y)
plt.grid()
plt.show()

# multi dimension : dot size(s)/color(c) to show depth ; bubble chart
n = 30
np.random.seed(0)
x = np.random.rand(n)
y1 = np.random.rand(n)
y2 = np.random.rand(n)
y3 = np.pi*(15*np.random.rand(n))**2
plt.scatter(x,y1,c=y2,s=y3)
plt.grid(True)
plt.show()