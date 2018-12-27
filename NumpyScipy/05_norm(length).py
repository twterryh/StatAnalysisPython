import numpy as np

# vector length : norm of vector
# ||a||
# = root a.T * root a

a = np.array([1,3])
print(np.linalg.norm(a))

# 3.1622776601683795

# 단위 벡터 (unit vector) : 길이가 1 인 벡터
# ex) [0,1], [0,1], [1/np.sqrt(2),1/np.sqrt(2)]
a = np.array([0,1])
print(np.linalg.norm(a))
