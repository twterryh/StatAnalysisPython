import matplotlib.pylab as plt
import numpy as np

# pie : 원 형태를유지하기 위해 plt.axis('equal') 을 먼저 실행해야 함

# pie(ratio(비율들),
#     explode(강조를 위한 옵션),
#     labels,
#     colors,
#     autopct(퍼센트로 환산),
#     shadow(그림자/입체감),
#     startangle(시작 각도))

labels = 'a','b','c','d'
ratio = [10,30,40,20]
colors = ['red','blue','yellow','green']
explode = (0,0.1,0,0)
plt.axis('equal')       # 동그란 원으로 그려줌
plt.pie(ratio,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90)
plt.show()