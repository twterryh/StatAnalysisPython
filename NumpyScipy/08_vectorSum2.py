import numpy as np
import matplotlib.pylab as plt

a = np.array([1,2])
b = np.array([2,1])
c = a+b

plt.plot(0,0,'go',ms=10)
plt.plot(a[0],a[1],'ko',ms=20)
plt.plot(c[0],c[1],'ro',ms=25)

plt.annotate('',xy=a,xytext=(0,0),arrowprops=dict(facecolor='red'))
plt.annotate('',xy=c,xytext=a,arrowprops=dict(facecolor='black'))

plt.show()