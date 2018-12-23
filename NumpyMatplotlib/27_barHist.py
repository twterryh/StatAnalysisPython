import numpy as np
import matplotlib.pylab as plt

# bar chart : bar(vertical(default) / barh(horizontal)
# bar(x axis, y axis)
y = [2,3,1]
x = np.arange(3)
xlabel = ['A','B','C']
plt.bar(x,y)
plt.xticks(x,xlabel)
plt.grid(True)
plt.show()

# barh
np.random.seed(0)
yLabel = ['A','B','C','D']
yPos = np.arange(4)
yValue = 2+10*np.random.rand(4)
plt.barh(yPos,yValue, alpha=0.5)    # alpha : 바의 투명도
plt.yticks(yPos,yLabel)     # 세로축이니 xticks 가 아니라 yticks
plt.grid(True)
plt.show()

# histogram
# hist
# bins : 데이터를 집계할 구간 정보 설정
np.random.seed(0)
x = np.random.randn(1000)
arrays, bins, patches = plt.hist(x, bins=10)     # 열개의 구간
print(arrays)
# [  9.  20.  70. 146. 217. 239. 160.  86.  38.  15.]
print(bins)
# [-3.04614305 -2.46559324 -1.88504342 -1.3044936  -0.72394379 -0.14339397
#   0.43715585  1.01770566  1.59825548  2.1788053   2.75935511]
print(patches)
# <a list of 10 Patch objects>
plt.show()