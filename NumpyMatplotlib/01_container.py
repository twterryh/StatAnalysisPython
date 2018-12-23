a: float = 3;
print(a)
print(type(a))

x = 1.1
print(type(x))

h = "hello"
print(h)
len(h)

'''
# containter

standard : list(different data types), tuple, dictionary, set

collections module : deque(양쪽 열려있음), defaultdict, counter, namedtuple, orderedDict
array module : (same data type)(memory-efficient) 
heapq module : (keep list in order -> reduce overhead)
bisect module (add/repeated value processing)
Queue
struct
copy

'''


'''
slicing : 리스트의 일부분
'''


# enumerate
animal = ['a', 'b', 'c']
for idx, anim in enumerate(animal):
    print('#%d %s' %(idx+1, anim))

# square
num = [0,1,2,3]
squ = []
for i in num:
    squ.append(i**2)

squ2 = [i**2 for i in num]

num2 = [5,2,31,5,3,5,3,2,4]
odd_squ = [x**2 for x in num2 if x%2==1]

# dictionary : (key, value)
d = {'cat': 'cute', 'dog':'furr'}

num1 = [1,2,4,5]
even_squ = {x: x**2 for x in num1 if x%2==0}


# items method : value of key
d = {'aa':10, 'bb':15,'cc':102}
for a, number in d.items():
    print('%s is %d' % (a,number))


# set (no order, {}) vs list (order)
animals = {'a','b'}
# set : does not support indexing, has no order, no recursive values
for idx, a in enumerate(animals):
    print('%d,,, %s' %(idx, a))
# added last, is first in set

from math import sqrt
num3 = {int(sqrt(x)) for x in range(30)}
# {0, 1, 2, 3, 4, 5} since integer

# tuple
d = {(a, a+1): a for a in range(10)}
# {(0, 1): 0, (1, 2): 1, (2, 3): 2, (3, 4): 3, (4, 5): 4, (5, 6): 5, (6, 7): 6, (7, 8): 7, (8, 9): 8, (9, 10): 9}

