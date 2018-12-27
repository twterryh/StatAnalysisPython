import numpy as np
import matplotlib.pylab as plt

# sum of vectors
a = np.array([1,2])
b = np.array([2,1])
c = a+b

plt.plot(0,0,'bo',ms=15)
plt.plot(a[0],a[1],'ro',ms=15)
plt.plot(b[0],b[1],'yo',ms=15)
plt.plot(c[0],c[1],'kp',ms=20)

plt.annotate('',xy=a,xytext=(0,0),arrowprops=dict(facecolor='red'))
plt.annotate('',xy=b,xytext=(0,0),arrowprops=dict(facecolor='blue'))
plt.annotate('',xy=c,xytext=(0,0),arrowprops=dict(facecolor='black'))

plt.plot([a[0],c[0]],[a[1],c[1]], 'r--')        # a 와 c 를 잇는 점선 그리기
plt.plot([b[0],c[0]],[b[1],c[1]], 'b--')

plt.text(0.4,1.2,'$a$',fontdict={'size':15})
plt.text(1.5,0.5,'$b$',fontdict={'size':15})
plt.text(1.4,1.6,'$c$',fontdict={'size':15})

plt.xticks(np.arange(-2,5))
plt.yticks(np.arange(-2,5))
plt.xlim(-0.5,3.5)
plt.ylim(-0.5,3.5)

plt.grid(True)
plt.show()