import numpy as np

# split = array_split
x = np.arange(9.0)
print(x)        # [0. 1. 2. 3. 4. 5. 6. 7. 8.]

print(np.split(x,3))
# [array([0., 1., 2.]), array([3., 4., 5.]), array([6., 7., 8.])]

x1 = np.split(x,3)
print(x1[0])        # [0. 1. 2.]
print(x1[1])        # [3. 4. 5.]
print(x1[2])        # [6. 7. 8.]

print(np.split(x, [3,4]))
# [array([0., 1., 2.]), array([3.]), array([4., 5., 6., 7., 8.])]
# 3번 앞에서 자르고, 4번 앞에서 자르고, 나머지

print(np.array_split(x, [1,5,6]))
# [array([0.]), array([1., 2., 3., 4.]), array([5.]), array([6., 7., 8.])]
# 1번 앞에서 자르고, 5번 앞에서 자르고, 6번 앞에서 자르고, 나머지


# dsplit : depth
y = np.arange(16).reshape(2,2,4)
print(y)
'''
[[[ 0  1  2  3]
  [ 4  5  6  7]]

 [[ 8  9 10 11]
  [12 13 14 15]]]
'''
y2 = np.dsplit(y,2)
print(y2)
print(np.shape(y2))     # (2, 2, 2, 2)
'''
[array([[[ 0,  1],
         [ 4,  5]],

        [[ 8,  9],
         [12, 13]]]), 

array([[[ 2,  3],
        [ 6,  7]],

       [[10, 11],
        [14, 15]]])]
'''

# hsplit : horizontally split : 좌측, 우측 으로 나눔
h = np.arange(16).reshape(4,4)
h2 = np.hsplit(h,2)
print(h2)
print(np.shape(h2))     # (2, 4, 2)
'''
[array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]]), 
array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])]
'''
# h3 = np.hsplit(h, [3,6]) : index 를 이용한 hsplit 도 가능 : 3 앞에서 자르고, 6은 없으니 나머지
# 다차원에서도 hsplit 쓸 수 있다 : 다차원에서는 수평선

# vsplit : vertically split : 상부, 하부 로 나눔
v = np.arange(16).reshape(4,4)
print(v)
print(np.vsplit(v, 2))
'''
[array([[0, 1, 2, 3],
       [4, 5, 6, 7]]), 
 array([[ 8,  9, 10, 11],
       [12, 13, 14, 15]])]
'''
# 다차원에서 vsplit 은 깊이를 자름
