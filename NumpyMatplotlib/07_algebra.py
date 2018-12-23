import numpy as np

# 연산자 or numpy ftn

x = np.array([[1,2],
              [3,4]], dtype = np.float64)
y = np.array([[5,6],
              [7,8]], dtype = np.float64)

print(2*x + y)
print(np.add(x,y))
print(np.subtract(x,y))
print(np.multiply(x,y))
print(np.divide(x,y))
print(np.sqrt(x))       # square root

print(x>3)             # bool
'''
[[False False]
 [False  True]]
'''
print(y>6)
'''
[[False False]
 [ True  True]]
'''
print((x>3) & (y>6))
'''
[[False False]
 [False  True]]
'''

print(np.sum(x))    # 10 = 1+2+3+4 : 모든 요소들의 합

print(np.sum(x, axis=0))    # [4. 6.] = [(1+3) (2+4)]
# axis = 0 : 각 column 에 대한 계산

print(np.sum(x, axis=1))    # [3. 7.] = [(1+2) (3+4)]
# axis = 1 : 각 row 에 대한 계산