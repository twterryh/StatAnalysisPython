import numpy as np

a = np.arange(8).reshape((2,2,2))
print(a)
'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''

# flip : 뒤집기 : flip(array, axis)
print(np.flip(a, 0))
'''
[[[4 5]
  [6 7]]

 [[0 1]
  [2 3]]]
'''

print(np.flip(a, 1))
'''
[[[2 3]
  [0 1]]

 [[6 7]
  [4 5]]]
'''

print(np.flip(a,2))
'''
[[[1 0]
  [3 2]]

 [[5 4]
  [7 6]]]
'''

print(np.flip(a))
'''
[[[7 6]
  [5 4]]

 [[3 2]
  [1 0]]]
'''


# fliplr : flip left/right
# diag : 대각선 배열을 만듬
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
print(np.fliplr(c)) # 좌우로
'''
[[0 0 1]
 [0 2 0]
 [3 0 0]]
'''
print(np.flipud(c)) # 위아래
'''
[[0 0 3]
 [0 2 0]
 [1 0 0]]
'''

# rot90 : rotation : 90도 회전
# 옵션 : k:회전 횟수 ; axes
d = np.array([[1,2],
              [3,4]])
print(np.rot90(d, 1, (0,1)))    # 0:가로 에서 1:세로 로 이동하는 방향
'''
그래서 반시계 방향으로 1회 이동한 것
[[2 4]
 [1 3]]
'''

print(np.rot90(d, 1, (1,0)))
'''
1(세로축) 에서 0(가로축) 방향으로 1회 이동
[[3 1]
 [4 2]]
'''