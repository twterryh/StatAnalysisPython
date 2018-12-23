import numpy as np

# slicing is available in numpy
a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])
print(a)

b = a[:2, :2]
print(b)

c = a[:2, 1:3]
print(c)

d = a[1:3, 1:3]
print(d)

b[0,0] = 100
print(b)
print(a) # a[0,0] ALSO CHANGES TO 100 !!

print(a.ndim)       # 2

e = np.array([[1,2,3]])
print(e)
print(e.ndim)       # 2 dimension
print(e.shape)      # (1,3) : 1 row, 3 columns

f = a[1, :]
print(f)
print(f.ndim)       # 1

f2 = a[1:2, :]
print(f2)
print(f2.ndim)      # 2

