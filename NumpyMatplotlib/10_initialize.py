import numpy as np

e = np.empty((4,3))
print(e)
# 4x3 matrix with garbage values is generated

o = np.ones((2,3,4))
print(o)
'''
[[[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]

 [[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]]
'''

o2 = np.ones_like(o, dtype="f")
print(o2)
'''
[[[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]

 [[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]]
'''

z = np.zeros((2,3,4))
print(z)


b = np.arange(9).reshape((3,3))
print(b)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
print(np.diag(b))       # [0 4 8]
print(np.diag(b, -1))   # [3 7]
print(np.diag(b, 1))    # [1 5]

c = np.diag([1,2,3])
print(c)
'''
[[1 0 0]
 [0 2 0]
 [0 0 3]]
'''