import numpy as np
import matplotlib.pylab as plt

# 차트에서 주석 처리
# annotate(s, xy ,xytext, xycoords, arrowprops, ... )
# s : 주석
# xy : 화살표의 시작 위치
# xytext : 주석 텍스트 시작 위치
# arrowprops : 화살표 모양/색상

ax = plt.subplot(111)   # 1 행 1 열 첫 번째
t = np.arange(0.0,5.0,0.01)
s = np.cos(2*np.pi*t)
line = plt.plot(t,s,lw=2)

plt.grid(True)
plt.annotate('max value',xy=(3,1),xytext=(3.5,1.5),arrowprops=dict(facecolor='red'))    # generate a red arrow
plt.ylim(-2,2)
plt.show()
