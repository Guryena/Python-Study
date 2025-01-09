from collections import deque, OrderedDict, defaultdict, Counter, namedtuple

"""
    collections 모듈: 파이썬의 내장 모듈
    (1) deque : 스택과 큐를 모두 지원하는 모듈
    (2) OrderedDict : 순서를 가진 딕셔러니 객체
    (3) defaultdict : 딕셔너리 변수를 생성할 때 키에 대한 기본 값을 지정
                  같은 이름의 키의 값을 하나로 만들 때 사용
    (4) Counter : 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조
    (5) namedtuple : 튜플의 형태로 데이터 구조체를 저장하는 방법
"""

#-------------------------------------
# (1) deque : 스택과 큐를 모두 지원하는 모듈
#           - 리스트와 비슷한 형식으로 데이타를 저장한다.
#           - append() 함수로 기존 리스트처럼 데이터가 인덱스 번호와 저장된다

deque_list = deque()
for i in deque_list:
    deque_list.append(i)

print(type(deque_list))
print(deque_list)
# deque_list.pop()
# deque_list.pop()
print(deque_list)
deque_list.insert(1, 100)
print(deque_list)
print()
# -------------------------------------------
# (2) OrderedDict 모듈 : 순서를 가진 딕셔러니 객체
#                기본적인 딕셔너리는 순서를 보장하지 않는 객체이다
d = {}
d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4
d["e"] = 5
for k, v in d.items():
    print(k, v)

print()

d = OrderedDict()
d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4
d["e"] = 5
for k, v in d.items():
    print(k,v)



#----------------------------------------------
# (3) defaultdict : 딕셔너리 변수를 생성할 때 키에 대한 기본 값을 지정
#                   같은 이름의 키의 값을 하나로 만들 때 사용

# d=dict()
# print(d['first'])
# [에러발생] - 생성하지 않은 키를 호출



d = defaultdict(lambda : 0) #If enter key value, default value is setting 0(return)
print(d["f"])

s = [("yellow"), 1]
#---------------------------------------------------
# (4) Counter 모듈 : 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조

text = list("Hello world")
c = Counter(text)
print(c, type(c))




#-------------------------------------------------
# (5) namedtuple : 튜플의 형태로 데이터 구조체를 저장하는 방법

myPoint = namedtuple("MyPoint", ["x","y"])
p = myPoint(100,200)
print(p)