import numpy as np

# unique    : 중복 제거 후 리스트 출력, (당연히) 나온 것만 출력한다
# unique 인수 중 return_counts = True : 데이터 개수도 출력해 줌
a = np.unique([1,1,2,2,3,3,3,2,2,4])
print(a)        # [1 2 3 4]

b = np.array(['a','b','b','c','a','d'])
b1 = np.unique(b)
print(b1)       # ['a' 'b' 'c' 'd']
b2 = np.unique(b, return_counts=True)
print(b2)
# (array(['a', 'b', 'c', 'd'], dtype='<U1'), array([2, 2, 1, 1], dtype=int64))
print(b2[0])    # ['a' 'b' 'c' 'd']
print(b2[1])    # [2 2 1 1]

data, count = np.unique(b, return_counts=True)
print(data)     # ['a' 'b' 'c' 'd']
print(count)    # [2 2 1 1]


# bincount : 나오지 않은 숫자도 count 를 0 으로 출력해줌
# bincount 인수 중 minlength 이용하면 편리함
# 주사위를 여러번 던져도 한번도 안 나온 수가 있을 때?
# 사례) 주사위를 6번 던졌는데, 1,1,2,2,3,4 이렇게 나왔을 때
print(np.bincount([1,1,2,2,3,4], minlength=6))
# [0 2 2 1 1 0]
