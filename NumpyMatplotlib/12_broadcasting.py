import numpy as np

# broadcasting
# allows algebra between arrays of different shapes by changing shapes
# 조건!
# 1) 한 쪽이 scalar 일 때 = when rank is 1
# 2) 차원의 짝이 맞을 때 : 축의 길이가 같을 때


a = np.array([1,2,3])
b = np.array([1,2])
# print(a+b)      # error : operands could not be broadcast together with shapes (3,) (2,)

c = 10
print(a+c)      # [11 12 13] = [1 2 3] + 10 = [1 2 3] + [10 10 10]
print(a*c)      # [10 20 30]

aaa = np.array([[1,2],
                [3,4]])
print(aaa+c)
'''
[[11 12]
 [13 14]]
'''

a = np.array([1,2,3])
aa = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(aa + a)
'''
[[ 2  4  6]
 [ 5  7  9]
 [ 8 10 12]]

a = [[1,2,3],
     [1,2,3],
     [1,2,3]] 로 broadcasting 됨
'''

x = np.array([[1],
              [2],
              [3]])
print(x.shape)      # (3, 1)
y = np.array([1,2,3])
print(y.shape)      # (3,)
print(x+y)
'''
[[2 3 4]
 [3 4 5]
 [4 5 6]]
둘 다 broadcasting 된 것!
'''

# 3d broadcasting
ddd = np.empty((3,4,2))
dd = np.empty((4,2))
print(ddd.ndim)
print(dd.ndim)  # 3
print(ddd+dd)   # 2
# result : (3,4,2) 로 dd 가 broadcasting 됨

