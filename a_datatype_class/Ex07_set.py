# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다
from itertools import product

s = set()               # 빈 집합을 생성
s = set([1,2,3,1,1])    ## set() function is delete to duplication
print(s)

s1 = {3,4,5,6,3}
print(type(s1))
print()

##교집합
print(s.intersection(s1))
print(s & s1)
print()

##합집합
print(s.union(s1))
print(s|s1)
print()

##차집합
print(s -s1)
print(s1 - s)
print()

##곱집합
s3 = list(product(s, s1))
print(s3)