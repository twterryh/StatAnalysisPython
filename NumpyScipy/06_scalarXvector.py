import numpy as np
import matplotlib.pylab as plt

a = np.array([1,2])

b = 2*a
c = -1*a

plt.plot(0,0,'ko',ms=10)

plt.annotate('',xy=a,xytext=(0,0),arrowprops=dict(facecolor='black'))
plt.text(0.2,1.2,"$a$",fontdict={"size":15})
plt.text(1.2,1.8,'$(1,2)$',fontdict={"size":15})

plt.annotate('',xy=b,xytext=(0,0),arrowprops=dict(facecolor='red'))
plt.text(0.9,3.2,'$2a$',fontdict={"size":15})

plt.annotate('',xy=c,xytext=(0,0),arrowprops=dict(facecolor='blue'))
plt.plot(c[0],c[1],'gp',ms=20)
plt.text(-1.2,-0.7,'$-a$',fontdict={"size":15})

plt.xticks(np.arange(-4,6))
plt.yticks(np.arange(-4,6))
plt.xlim(-4.5,5.5)
plt.ylim(-3.5,5.5)

plt.grid(True)
plt.show()
