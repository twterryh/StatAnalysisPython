import numpy as np
import matplotlib.pylab as plt

plt.plot(0,0,'kP', ms=10)           # 원점 찍기 : k:black, P:+, ms(marker size)

a = np.array([1,3])
plt.plot(a[0],a[1],'bo',ms=5)       # a 찍기 : b:blue, o:o figure

plt.annotate('',xy=a,xytext=(0,0),arrowprops=dict(facecolor='yellow'))  # draw arrow
# plt.annotate('a=(1,3)',xy=(1,3),xytext=(1.1,3.2))                         # write annotation

# you can also use plt.text()
plt.text(0.1,1.5,'$a$',fontdict={"size":20})               # italicize
plt.text(1.1,3.2,'a=(1,3)',fontdict={"size":20})

# 화살표 평행 이동 / 텍스트 이동
plt.annotate('',xy=a+[-1,1],xytext=(-1,1),arrowprops=dict(facecolor='green'))
plt.text(-0.9,2.5,'$a$',fontdict={"size":25})

plt.xticks(np.arange(-2,5))
plt.yticks(np.arange(-1,5))
plt.xlim(-2.5,4.4)
plt.ylim(-0.6,4.4)

plt.grid(True)
plt.show()

