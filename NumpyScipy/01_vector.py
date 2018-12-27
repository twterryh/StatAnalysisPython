import numpy as np

# vector 를 numpy 에서 표현하기 : 열의 개수가 1 인 2차원 배열 객체
# 1차원 배열 객체도 vector 로 인정하기는 함
# but, 더 직관적인 게 2차원 (n rows, 1 column) 인 건 맞음

x1 = np.array([[2.1],[2.4],[0.3]])
print(x1)
'''
[[2.1]
 [2.4]
 [0.3]]
'''
print(np.shape(x1))     # (3,1)

# a single data record in a matrix : row data : 한 행에 한 레코드
# a single data record as a vector : column data : 한 레코드는 여러 행, 한 열

# zero vector
print(np.zeros((5,1)))