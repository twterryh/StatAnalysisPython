import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt

# matplotlib : data visualization package
# line plot, scatter plot, bar chart, histogram, etc.

# (subpackages)
# pylab : metlab lang

# line plot : time series
'''
plt.plot([1,5,8,15])    # ndarray 를 반환 : (0,1), (1,5), (2,8), (3,15) 가 찍힘 : "tick" 이라고 부름
plt.grid(True)          # 격자
plt.show()              # chart rendering
'''

plt.plot([1,2,9,10,30],         # x axis
        [30,59,48,399,102], 'rs--')     # y axis
plt.show()

'''
plt.plot([[1,2,9,10,30],
          [30,59,48,399,102]])
plt.show()

'''

# chart style
# color, marker, line style
# ' r      s         --'
# ' red  square
# color : r(red), m(magenta), c(cyan), etc...
# marker : 좌표 : s(square), +, d(diamond)


# Matplotlib 그림 : Figure, Axes, Axis 로 구성됨.
# Figure 객체는 Matplotlib.figure.Figure class 에 포함됨.
# Axis 도 Figure class 하위에 있는 객체
# Axis 둘 이상을 합쳐서 Axes 라고 부름
# Axes : 하나의 plot
# Figure : plot 이 그려지는 canvas 라고 이해하자


# subplot : 하나의 Figure/window/canvas 안에 여러 개의 plot(axes) 을 배열 형태로 보이도록 함
# Figure 안에 Axes 을 생성하려면 subplot 명령을 사용해서 Axes 객체를 얻어야 함
# plot 명령을 이용해도, Axes 를 생성할 수 있음

# subplot(row, column, select)
# 'row' rows of plots, 'column' rows of plots, 'select' index of plot

# tight_layout : plot 사이 간격 자동 조절