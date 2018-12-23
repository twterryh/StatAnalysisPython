import numpy as np

# product
# dot() : product

x = np.array([[1,2],
              [3,4]])
y = np.array([[5,6],
              [7,8]])
v = np.array([9,10])
w = np.array([11,12])

# product of vectors
print(v.dot(w))     # 219 = 9*11 + 10*12 = v[0]*w[0] + v[1]*w[1]
print(np.dot(v,w))  # 219

# product of matrix and vector
print(x.dot(v))     # [29 67] : (rank 1) x*v
print(np.dot(x,v))  # [29 67]
print(v.dot(x))     # [39 58]

# product of matrices (교환법칙 성립 x)
print(x.dot(y))
print(np.dot(x,y))
print(x.dot(y).ndim)    # (rank 2)
'''
[[19 22]
 [43 50]]
'''
print(y.dot(x))
print(np.dot(y,x))
'''
[[23 34]
 [31 46]]
'''
