"""
    [ 함수 ]

     반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다

     def 함수명(매개변수):
        수행할 문장들
"""
from operator import index


def testFunc():
    print("output func")


testFunc()


def testFunc2(x, y):
    return x + 5, x - 5


print(testFunc2(5, 5))
print(type(testFunc2(5, 5)))
a, b = testFunc2(10, 10)
print(a + b)
print("------------------------------------------------")


##positional argument
def func(greeting, name):
    print(greeting, "!!!", name, ".sir")


func("x", "y")
print()


def func(x, y, z=100):
    print(x)
    print(y)
    print(z)


func(10, 5, 20)
print()
func(10, 5)

print()

def buggy(x, result=[]):
    result.append(x)
    print(result)
    print(id(result))
buggy("a")
buggy("b")
buggy("c")
buggy("A", result=[1,2,3,4]) ## If create new list, used new memory id
aList = [1,2,3,4,5] ##If used different memory id, create new list to function outside
buggy("B")
buggy("C", result=["1"])

'''
    1번째와 2번째는 인자가 반드시 들어가고 3번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
    그러나 4번째 인자부터는 정확히 모른다면?
    print(func(4, 5))
    print(func(4, 5, 6))
    print(func(4, 5, 6, 7))
    print(func(4, 5, 6, 7, 8, 9))       # i9에 7,8,9가 튜플로 들어간다
    '''
print("------------------------------------------------")

#positional arguments(*args)
# *args = 미정의 값을 줄 때/ 특히 다수의 값을 넣을지 모르는 상황에
def func(i1, i2, i3 = 0, *args):
    sum = i1+i2+i3
    for i in args:
        sum += i
    return sum
print(func(1, 2,3, 5))
print()
#keyword arguments(**kwargs)
def func(i, j , k = 100, *args, **kwargs):
    print(args)     #*args is type tuple()
    print(kwargs)   #**kwargs is type dictionary{}
func(1, 2)
print()
func(1, 2, 3, 4, 5, a=6, b=7, d=8)

def getSum(x=0, y=0 , z = 100, *args, **kwargs):
    sum = x + y + z
    try:
        values = list(kwargs.values())
        for i in values:
            sum += int(i)
        for j in kwargs.values():
            sum += int(j)
        # for i in range(len(args)):
        #     sum += int(args[i])
        # for j in range(len(kwargs)):
        #     sum += int(values[i])

        return print(sum)
    except:
        return print(sum)

getSum(1, 2, 3, 4, 5, a=6, b=7, d=8)
# getSum(1, 2, 3, 4, 5)
# getSum(1, 2, 3)
# getSum(1)