import numpy as np

# array indexing = fancy indexing
# select/change a single value from each row

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9],
              [10,12,14]])
print(a)

# indexes
idx = np.array([0,2,0,1])
print(a[np.arange(4),idx])
# [ 1  6  7 12] : [(0,0) (1,2) (2,0) (3,1)]
# arange : [0 1 2 3]

a[np.arange(4),idx] *= 2
print(a)
'''
[[ 2  2  3]
 [ 4  5 12]
 [14  8  9]
 [10 24 14]]
 원하는 값들만 두배 했다
 1->2, 6->12, 7->14, 12->24
 '''

# extract even!
b = np.array([0,1,2,3,4,5,6,7,8,9])
idx2 = np.array([True, False, True, False, True, False, True, False, True, False])
print(b[idx2])      # [0 2 4 6 8]
print(b[b%2==0])    # [0 2 4 6 8] : 조건을 이용해서 할 수 있다

