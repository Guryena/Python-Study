"""
        숫자형 종류
            - 정수형
            - 실수형
            - 복소수형 1 + 2j, 3i  ( 많이 사용안함 )
            - 8진수   0o25
            - 16진수  0x25
"""
from xmlrpc.client import boolean

# 파이션의 모든 자료형은 객체로 취급한다
# 실행 : alt + shift + F10

""" [ 기초 연산자 ]
        + : 더하기
        - : 빼기
        * : 곱하기
        / : 나누기(실수값 결과)
        // : 나누기(정수값 결과)
        % : 나머지
        ** : 제곱
    
    2. 관계연산자
        <   >   <=  >=  ==  !=
    
    3. 논리연산자
        not     or      and
        
    4. 이진(비트) 연산자
        ~   :  이진 not   
        |   :  이진 or
        &   :  이진 and
        ^   :  이진 xor
        <<  :  shift
        >>  :  shift
        
    5. 대입연산자
        =
        +=  -=  *=  /=  //= %=
        &=  |=  ^=
        >>= <<=
    
    6. 기타연산자 : 딕셔너리, 문자열, 리스트, 튜플 등의 자료형에서 사용
        is      : 비교하는 객체의 주소가 같으면 true, 다르면 false
        is not  : 비교하는 객체의 주소가 다르면 true, 같으면 false 
        in      : 요소에 포함되면 true, 없으면 false
        not in  : 요소에 포함되지 않으면 false, 없으면 true
      

    [참고] 증가(++), 감소(--) 연산자 없음         
"""

a = 5
b = 2

""" [ 출력결과 ] 
        a + b = 7
        a - b = 3
        a * b = 10
        a / b = 2.5
        a // b = 2
        a % b = 1
        a ** b = 25
"""
a = 7
b = 7

print(type(7))
print(a == 71)
print(b is a)

a, b = 1, 5
print(a, b)
a, b = b, a
print(a, b)

print("a = %d" % a, '\n', "b = %d" % b)


def a(b):
    x = 10
    c = 0
    if x > b:
        return True
    elif x == b:
        return c
    else:
        return False


print(a(11))

a = 7
b = 2


class cal:
    def plus(x, y):
        return x + y

    def minus(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

    def div_n(x, y):
        return x // y

    def dev2(x, y):
        return x % y

    def sqr(x, y):
        return x ** y

    print(plus(a, b))
    print(div(a, b))


import math

print(a ** b, type(a ** b))
c = 7.2
d = 2.5
print(c ** d, type(c ** d))

print()

print(math.pow(a, b), type(math.pow(a, b)))
print(math.pow(c, d), type(math.pow(c, d)))

print()

print(pow(a, b), type(pow(a, b)))
print(pow(c, d), type(pow(c, d)))

print()

print("{0}".format(c**d))
print(f"ㅁㄴㅇㄹ : {c**d} adf. fa = {a**b}")