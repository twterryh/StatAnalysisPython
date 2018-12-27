import numpy as np
import matplotlib.pylab as plt

a = np.array([1,2])
b = np.array([2,1])
c = a-b

plt.annotate('',a,(0,0),arrowprops=dict(facecolor="blue"))
plt.annotate('',b,(0,0),arrowprops=dict(facecolor="red"))
plt.annotate('',a,b,arrowprops=dict(facecolor="yellow"))

plt.plot(0,0,'go',ms=10)
plt.plot(a[0],a[1],'ro',ms=20)
plt.plot(b[0],b[1],'yo',ms=15)

plt.text(0.2,1.2,"$a$",fontdict={'size':15})

plt.grid(True)
plt.show()

print(c)

