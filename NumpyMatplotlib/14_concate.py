import numpy as np

# 행의 수, 열의 수가 같은 두개 이상의 배열 연결
# concatenate : hstack, vstack, dstack, stack, r_, c_, tile

# hstack (horizontal) : concate columns : 행의 수가 같아야 함
a1 = np.ones((2,3))
a2 = np.zeros((2,2))
# 열의 수는 각각 3, 2 = 합쳐서 열의 수 5 됨
a3 = np.hstack([a1,a2])
print(a3)
'''
[[1. 1. 1. 0. 0.]
 [1. 1. 1. 0. 0.]]
'''

# vstack (vertical) : concate rows : 열의 수가 같아야 함
b1 = np.ones((2,3))
b2 = np.zeros((3,3))
# 행의 수가 각각 2, 3 = 합쳐서 행의 수 5 됨
b3 = np.vstack([b1,b2])
print(b3)
'''
[[1. 1. 1.]
 [1. 1. 1.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
'''

# dstack (depth) : 깊이 방향으로 배열 합침 : 헷갈리게 합쳐진다!
c1 = np.ones((3,4))
c2 = np.zeros((3,4))
c3 = np.dstack([c1,c2])
print(c3)
'''
[[1. 0.]
 [1. 0.]
 [1. 0.]
 [1. 0.]]
*3 
'''
print(c3.shape)     # (3,4,2)

# stack : 그냥 면만 추가됨 : 연결하고자 하는 배열들의 크기가 같아야 함
# 인수로 axis 사용할 수 있음 (default : 0)
c4 = np.stack([c1,c2])
print(c4)
'''
[[[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]
'''
print(c4.shape)     # (2,3,4)

c5 = np.stack([c1,c2], axis=1)  # row
print(c5)
'''
[[[1. 1. 1. 1.]
  [0. 0. 0. 0.]]

 [[1. 1. 1. 1.]
  [0. 0. 0. 0.]]

 [[1. 1. 1. 1.]
  [0. 0. 0. 0.]]]

(3,2,4)
'''

c6 = np.stack([c1,c2], axis=2)  # column
print(c6)
'''
[[[1. 0.]
  [1. 0.]
  [1. 0.]
  [1. 0.]]

 [[1. 0.]
  [1. 0.]
  [1. 0.]
  [1. 0.]]

 [[1. 0.]
  [1. 0.]
  [1. 0.]
  [1. 0.]]]
  
(3,4,2)
'''

# r_ (method) : similar to hstack, 배열을 좌우로 연결, () 사용 x, [] 사용 ==> indexer
# c_ (method) : 배열 차원 증가시킨 후, 좌우로 연결
d1 = np.array([1,2,3])
d2 = np.array([4,5,6])

print(np.r_[d1,d2])     # [1 2 3 4 5 6]
print(np.r_[d2,d1])     # [4 5 6 1 2 3]

print(np.c_[d1,d2])
'''
[[1 4]
 [2 5]
 [3 6]]
'''

# tile : 동일한 배열 반복 연결
t1 = np.array([[0,1,2],
               [11,12,13]])
print(np.tile(t1, 2))
'''
[[ 0  1  2  0  1  2]
 [11 12 13 11 12 13]]
'''

print(np.tile(t1, (3,2)))
'''
3행 2열로 t1 반복
[[ 0  1  2  0  1  2]
 [11 12 13 11 12 13]
 [ 0  1  2  0  1  2]
 [11 12 13 11 12 13]
 [ 0  1  2  0  1  2]
 [11 12 13 11 12 13]]
'''

# column_stack, row_stack
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.column_stack((a,b)))
'''
[[1 4]
 [2 5]
 [3 6]]
'''
print(np.row_stack((a,b)))
'''
[[1 2 3]
 [4 5 6]]
'''


# repeat : similar to tile
xx = np.array([[1,2],
               [3,4]])
print(np.repeat(xx,2))          # [1 1 2 2 3 3 4 4]
print(np.repeat(xx,3))          # [1 1 1 2 2 2 3 3 3 4 4 4]
print(np.repeat(xx,3,axis=1))
'''
[[1 1 1 2 2 2]
 [3 3 3 4 4 4]]
'''
print(np.repeat(xx,3,axis=0))
'''
[[1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]
'''