def hi():
    print("hihi")
    print("more to")
    print("print")

hi()

def hi2(object):
    print("hi!" + object)

hi2('aaaa')


def hi3(a):
    print(type(a))

hi3(3)      # int
hi3('a')    # str
hi3('3')    # str


# class
class Person :
    def __init__(self, name):   # 생성자 : 클래스를 초기화하는 메서드
        self.name = name
        print("call >>")

    def hello(self):
        print("hello" + self.name + "!")

    def bye(self):
        print("byebye" + self.name + "!")

p1 = Person("kim")
p1.hello()
p1.bye()

