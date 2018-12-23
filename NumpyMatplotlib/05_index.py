import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
print(a)

b = a[[0,1,2],[0,1,0]]
print(b)         # [1 4 5] : (0,0), (1,1), (2,0)

c = np.array([1,2,3,4,5,6,7,8,9])
idx = np.array([0,0,0,0,1,1,1,2,2])

print(c[idx])
print(c[[0,0,0,0,1,1,1,2,2]])
# c[0] = 1, c[0] = 1, c[1] = 2, c[2] = 3
# thus, [1 1 1 1 2 2 2 3 3]

a = np.array([[1,2],
              [3,4],
              [5,6]])
c = a[[0,0],[1,1]]
print(c)    # [2,2] : a[0,1]=2, a[0,1]=2

d = a[0,1]
print(d)    # 2 : a[0,1]=2

# e = a[[rows], [columns]]
e = a[[0,1,2,1,2],[0,0,1,1,0]]
print(e)    # [1 3 6 4 5] = [(0,0) (1,0) (2,1) (1,1) (2,0)]

f = a[:,[True,False]]
print(f)
'''
[[1]
 [3]
 [5]]
 first column is True, second is False
'''