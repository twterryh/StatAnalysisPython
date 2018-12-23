import numpy as np

print(np.random.rand())     # 0 과 1 사이 무작위

# seed : 바꿔줘야 진정한 난수 발생 가능
np.random.seed(0)           # 0 번 난수표에서
print(np.random.rand(5))    # 난수 다섯개 생성 -> array

# shuffle data
x = np.arange(10)
np.random.shuffle(x)
print(x)
# [3 1 8 7 9 0 6 4 2 5] : 무작위 셔플, 할 때마다 달라짐

# random sampling
# choice(raw data, sample size, replace=True/False(복원/비복원), p(prob of choice))
y = np.random.choice(5, 6,replace=True)     # 복원 : 복원 추출이라 raw>sample 가능
print(y)
y = np.random.choice(5, 3,replace=False)    # 비복원
print(y)
y = np.random.choice(5, 10, p=[0.2,0,0,0.3,0.5])    # sum of prob must be 1
print(y)
# [0 4 3 4 4 4 4 4 4 4] : 4 가 나올 확률이 높은 만큼 추출된 것을 확인할 수 있다


# rand      : 0 ~ 1, uniform dist

# randn     : gaussian standard normal dist
a = np.random.randn(10,10,10)
print(a)
print(np.mean(a))       # when n->infinity, mean->0

# randint   : uniform dist, random integers
# randint(low, high, size)
# high 가 없으면, low 와 0 사이 숫자
# high 가 있으면, low 와 high 사이 숫자
# size 는 난수 개수
b = np.random.randint(10,size=8)
print(b)        # [0 3 2 2 2 3 5 1]
b1 = np.random.randint(10,20,8)
print(b1)       # [17 15 13 19 13 10 16 13]
b2 = np.random.randint(10,20,(5,5))
print(b2)
'''
[[16 19 15 11 19]
 [13 13 19 17 18]
 [14 17 18 19 14]
 [11 15 10 13 16]
 [13 10 13 16 19]]
'''

