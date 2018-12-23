import numpy as np

# same data type !! (!= list)

# scientific calculation (numerical analysis)
# data analysis
# statistics
# matrix algebra (multi dimension : ndarray)

# data type : float, complex, int, bool, string, object

# rank : 배열의 차원 : ex) 2D, 3D, .. : use 'ndim'
# shape : 각 차원의 크기를 튜플로 표시
# dtype : 저장된 자료를 알려줌 : ndarray.dtype.name

# ndarray : multi D array object


# rank : 1
a = np.array([1,2,3])
print(a)
print(type(a))      # numpy.ndarray
print(a.shape)      # (3,) : 3 rows : size of vector
print(a.ndim)       # 1 : 1 dimension : rank = 1


# rank : 2
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.shape)      # (2,3) : 2 rows, 3 columns
print(b.ndim)       # 2
print(b.dtype)      # int32
print(b.dtype.name) # int32
print(b.itemsize)   # 4 : 4bit : 한 요소가 차지하는 크기


# arange().reshape()
arr = np.arange(12)     # [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(arr)
arr = arr.reshape(4,3)
print(arr)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
 '''
print(arr.shape)    # (4,3)
print(arr.itemsize) # 4


# zeros() : 0행렬
# ones() : 1만 있는 행렬
b = np.zeros((2, 3))
print(b)
c = np.ones((2, 3))
print(c)


# full()
d = np.full((3,3), 10)
print(d)
'''
[[10 10 10]
 [10 10 10]
 [10 10 10]]
'''


# eye() : 단위행렬
e = np.eye(3)
print(e)
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''


# random()
f = np.random.random((2,2))
print(f)

aa = np.arange(0,10,2)
print(aa)       # [0 2 4 6 8]