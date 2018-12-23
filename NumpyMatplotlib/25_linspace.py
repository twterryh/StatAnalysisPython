import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt


# np.linspace(start, stop, number of samples(default=50), endpoint=True, retstep(샘플 간 간격)=False, dtype)

print(np.linspace(2.0,3.0,num=5))
# [2.   2.25 2.5  2.75 3.  ]    : endpoint == stop

print(np.linspace(2.0,3.0,num=5,endpoint=False))
# [2.  2.2 2.4 2.6 2.8]         : endpoint != stop

a,step = np.linspace(2.0,3.0,num=5,retstep=True)
print(a)    # [2.   2.25 2.5  2.75 3.  ]
print(step) # 0.25

a,step = np.linspace(2.0,3.0,num=5,endpoint=False,retstep=True)
print(a)    # [2.  2.2 2.4 2.6 2.8]
print(step) # 0.2

N = 8
y = np.zeros(N)
x1 = np.linspace(0,10,N,endpoint=True)
print(x1)
# [ 0.  1.428  2.857  4.285  5.714  7.1428  8.571 10.]
x2 = np.linspace(0,10,N,endpoint=False)

plt.plot(x1,y, 'o')
plt.plot(x2,y+0.4,'o')

plt.ylim([-0.5,1])   # y 축이 보이는 부분이 0.2 ~ 1 이 됨 (y 축 범위 지정) (xlim)
plt.show()

xx1 = np.linspace(0.0,5.0)
print(xx1)  # 0 에서 5 까지 일정한 간격으로 50개로 나뉘어서 출력
xx2 = np.linspace(0.0,2.0)

yy1 = np.cos(2*np.pi*xx1)*np.exp(-xx1)
yy2 = np.cos(2*np.pi*xx2)

ax1 = plt.subplot(2,1,1)
plt.plot(xx1,yy1,'ro-')
ax2 = plt.subplot(2,1,2)
plt.plot(xx2,yy2,'b.-')

plt.show()