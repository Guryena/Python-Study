"""
#----------------------------------------------------------
[튜플 자료형]
    1- 리스트와 유사하지만 튜플은 값을 변경 못한다.
    2- 각 값에 대해 인덱스가 부여
    3- 변경 불가능 (*****)
    4- 소괄호 () 사용
"""

# (1) 튜플 생성
print('------------------- 1. 튜플 생성-----------------')
t = (1, 2, 3)
print(t)
print(t[2])

t = 1,
print(type(t))
print(t)
# (2) 튜플은 요소를 변경하거나 삭제 안됨
# t[1] = 0;  # 블럭이 생기면서 실행 안됨
# del t[1]   # 에러 발생
print('------------------- 2 -----------------')

# (3) 하나의 요소를 가진 튜플
print('------------------- 3 -----------------')

# (4) 인덱싱과 연산자
print('------------------- 4 -----------------')
t = (1, 2, 3)
print(t[1:3])
t1 = (4, 5)
print(t + t1)
print(t * 3)
print()

##튜플 나누기
print(t)
n1, n2, n3 = t
print(n1+n2+n3)

##tuple exchange list
aList = [1,2,3]
aTuple = ('a', 'b', 'c')
print(tuple(aList))
print(list(aTuple))

a = [0, 1,2, 3, 4]
print(a[:3], a[:-3])
print(a[::-1])

a=1
b=1
print(a is b)
a=300
b=300
print(a is b)

list_1 = [[1, 2], [3], [4, 5, 6]]
a,b,c = list_1
list_2 = a + b + c
print(list_2)