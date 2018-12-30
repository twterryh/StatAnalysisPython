import numpy as np
import matplotlib.pylab as plt

X = np.linspace(-np.pi,np.pi,256)
C = np.cos(X)
plt.plot(X,C)

# tick : plot/chart 에서 축 상의 위치 표시 지점을 위미
# tick 에 쓰는 숫자/글자 : tick label
# tick label 은 Matplotlib 가 자동으로 정해줌
# 물론 사용자 지정 가능 (x axis, y axis 설정)

# tick label 을 수학 기호로 표시 : $$ 사이에 LaTeX('라텍') 문자를 넣어 사용

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           ['$-\pi$', '$-\pi/2$','$0$','$\pi/2$','$\pi$'])
plt.yticks([-1,0,1],
           ["Low","0","High"])
plt.grid(True)
plt.show()

# -------------------------------------------------
t = np.arange(1,10,0.1)
y = np.sin(t)
z = np.cos(t)

plt.figure(figsize=(14,14))
plt.plot(t,y, label='sin', lw=3)
plt.plot(t,z, label='cos', 'r')
plt.xlabel('time')
plt.ylabel('sin')
plt.title('hello')
plt.show()
