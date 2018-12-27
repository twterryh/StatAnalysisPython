import numpy as np

# 행과 열을 바꾸는 연산
# transpose : 전치 행렬

x = np.array([[1,2,3],
              [3,4,5],
              [7,8,9]])
print(x.T)
'''
[[1 3 7]
 [2 4 8]
 [3 5 9]]
'''

x1 = np.array([[2.1],[2.3],[2.4]])
print(x1)
'''
[[2.1]
 [2.3]
 [2.4]]
 '''
print(x1.T)             # [[2.1 2.3 2.4]]
print(np.shape(x1.T))   # (1, 3)

# T 는 method 가 아니라 속성 으로 봐야 함 : ()가 없음
# 1 차원 ndarray 는 전치 연산이 정의되지 않음

# square matrix (정방 행렬) : n * n
# diagonal matrix (대각 행렬) (D)
# identity matrix (diag + ones) (I)
i = np.identity(3)
print(i)
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''
i2 = np.eye(3)
print(i2)
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''

# symmetric matrix (대칭 행렬) : X = X.T (must be square)

