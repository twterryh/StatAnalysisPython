import numpy as np

# dtype 접두사
# b : boolean
# i : integer               ex) i4 (-> 32bit)
# u : 부호 없는 integer      ex) u8 (-> 64bit)
# f : real number           ex) f8 (-> 64bit)
# c : complex number        ex) c16 (-> 128bit)
# 0 : object pointer
# S : byte character        ex) S24 (-> 24 characters)
# U : unicode character     ex) U24 (-> 24 characters)

# Inf : infinity
# NaN : not a number
# N/A : not available

x = np.array([1,2,3])
print(x.dtype)      # int32

y = np.array([1,2,3.0])
print(y.dtype)      # float64

z = np.array([1,2,3], dtype = "f8")
print(z.dtype)      # float32

a = np.array([1,2,3], dtype = "U")
print(a)            # ['1' '2' '3']
print(a.dtype)      # <U1
print(a[0]+a[1])    # 12

i = np.array([0,1,-1,0])/np.array([1,0,0,0])
print(i)            # [  0.  inf -inf  nan]

