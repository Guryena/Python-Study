"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""


class Sample:
    ##생성자
    def __init__(self):
        self.age=22
        self.name = "Tim"
        print("function __init__")
    def setData (self, first, second):
        self.first = first

        self.second = second

        return first
s = Sample()
print(s.age)
print(s.setData(1,2))




print()








"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
    static  함수 :  클래스명 접근을 하며 객체끼리의 공유하고자 하는 메소드
    
    - 클래스 함수와 스태틱 함수는 둘 다 클래스명 접근
    - 클래스 함수는 cls를 이용하여 객체를 이용할 수 있다

"""

class Book:
    cnt = 0
    def __init__(self, title):
        self.title = title

    def output(self):
        print(f"제목 : {self.title}")
        self.cnt

##클래스 메서드는 특정 객체에 대한 작업을 처리하는 것이 아니라, 클래스 전체가 공유
    ##클래스 내의 변수를 공용으로 쓰기 위해
    @classmethod
    def output2(cls):
        cls.cnt += 1
        print(f"총 권수 : {cls.cnt}")

##정적 메서드는 클래스에 포함되는 단순한 유틸리티 메서드이다.
##특정 객체에 소속되지도 않고, 클래스와 관련된 동작을 하는 것도 아니어서 따로 self 또는 cls와 같은 인수를 받지 않는다.
    ##클래스 내 고정형으로 쓰기 위해
    @staticmethod
    def output3():
        print("bye")


b1 = Book("Hello world")
b1.output()
b1.output2()
b1.output3()
b2 = Book("Hi world")
b2.output()
b2.output2()
b2.output3()
print()

'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''

class Animal:
    def move(self):
        print("Animal is move")


class Wolf(Animal):
    def move(self):
        super().move()
        print(f"Wolf is run to 4foot")

class Human(Animal):
    def move(self):
        print("Human is run to 2foot")

w = Wolf()
w.move()
print(id(w.move()))
a = Animal()
a.move()
print(id(a.move()))
h = Human()
h.move()
print(id(h.move()))