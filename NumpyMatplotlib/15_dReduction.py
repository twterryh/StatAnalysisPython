import numpy as np

# 차원 축소 연산 (dimension reduction)
# 하나의 행의 원소들을 하나의 데이터 집합으로 보고
# 해당 행에 대한 연산을 하는 것

# min, max, argmin(최소값의 위치), argmax(최대값의 위치)
# sum, mean, median, std, var
x = np.array([1,10,100])

print(x.min())      # 1
print(x.max())      # 100

print(x.argmax())   # 2
print(x.argmin())   # 0

print(x.mean())     # 37.0
print(np.median(x)) # 10.0
print(x.std())      # 44.69899327725402
print(x.var())      # 1998.0

# all(배열의 모든 원소가 True 인지?), any(하나라도 True 있는지?)
print(np.all([True, True, False]))  # False
print(np.any([True, True, False]))  # True

# axis 도 차원 축소
y = np.array([[1,1],
              [2,2]])
print(y.sum())            # 6
print(y.sum(axis=0))      # [3 3] : 열 끼리 합친다
print(y.sum(axis=1))      # [2 4] : 행 끼리 합한다

