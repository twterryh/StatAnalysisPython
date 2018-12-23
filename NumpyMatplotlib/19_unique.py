import numpy as np

# unique
# non recursive data

a = np.array([1,1,2,3,1,2,2,3,1])
print(np.unique(a))
# [1 2 3]

b = np.array([[1,1],
              [2,3]])
print(np.unique(b))
# [1 2 3]

c = np.array([[1,0,0],
              [1,0,0],
              [2,3,4]])
print(np.unique(c))             # [0 1 2 3 4]
print(np.unique(c, axis=0))     # 중복되는 행 제거
'''
[[1 0 0]
 [2 3 4]]
'''
