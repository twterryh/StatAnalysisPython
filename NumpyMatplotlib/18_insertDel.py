import numpy as np

# delete

a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])

# remove one value : index 1 : remove 2
a1 = np.delete(a, 1)
print(a1)
# [ 1  3  4  5  6  7  8  9 10 11 12]

# remove row : remove row 2 : axis 0
print(np.delete(a,1,0))
'''
[[ 1  2  3  4]
 [ 9 10 11 12]]
'''

# remove column : remove column 1 : axis 1
print(np.delete(a,0,1))
'''
[[ 2  3  4]
 [ 6  7  8]
 [10 11 12]]
'''

# insert
b = np.array([[1,1],
              [2,2],
              [3,3]])

print(np.insert(b, 1, 100))
# [  1 100   1   2   2   3   3]

# insert column : axis = 1
print(np.insert(b, 1, 100, axis=1))
'''
[[  1 100   1]
 [  2 100   2]
 [  3 100   3]]
'''

# insert row : axis = 0
print(np.insert(b, 1, 100, axis=0))
'''
[[  1   1]
 [100 100]
 [  2   2]
 [  3   3]]
'''

# insert column with different values
print(np.insert(b, 1, [100,200,300], axis=1))
'''
[[  1 100   1]
 [  2 200   2]
 [  3 300   3]]
'''


# append
c = np.array([[1,2,3],
              [4,5,6]])

# print(np.append(c,[7,8,9],axis=0))      # error
print(np.append(c,[[7,8,9]],axis=0))      # 2 차원임을 맞춰줘야 한다
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''


# resize
x = np.array([[0,1],
              [2,3]])

# (2,2)인 x를 (2,3)으로 resize
print(np.resize(x,(2,3)))
'''
[[0 1 2]
 [3 0 1]]
 기존 0, 1, 2, 3 이 반복됨
'''


# trim_zeros : 좌우에 0 제거
z = np.array([0,0,0,1,2,3,0,1,2,0,0])
print(np.trim_zeros(z))
# [1 2 3 0 1 2] : 양 끝에 0 들이 제거됨 : 사이에 있는 0 은 안 지워짐

print(np.trim_zeros(z, 'f'))
# [1 2 3 0 1 2 0 0] : front 에 있는 0 들이 제거됨, 'b' : back
