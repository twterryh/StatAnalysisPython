import matplotlib.pylab as plt
import numpy as np

# 삼각 그리드 지원 패키지
import matplotlib.tri as mtri

# 삼각 그리드 생성
# Triangulation 클래스
# Triangulation(x, y, triangles)
# triangles(위치정보) 생략하면 자동생성

x = np.array([0,1,2])
y = np.array([0,np.sqrt(3),0])
triangles=[[0,1,2]]
triang = mtri.Triangulation(x,y,triangles)
plt.triplot(triang,'ro-')
plt.xlim(-0.1,2.1)
plt.ylim(-0.1,1.8)
plt.grid(True)
plt.show()

# 삼각형 여러 개 그리기
x = np.array([0,1,2,3,4,2])
y = np.array([0,np.sqrt(3),0,np.sqrt(3),0,2*np.sqrt(3)])
triangles=[[0,1,2],[2,3,4],[1,2,3],[1,3,5]]     # 삼각형에 선택할 index 들
triang = mtri.Triangulation(x,y,triangles)
plt.triplot(triang,'bo-')
plt.grid(True)
plt.show()