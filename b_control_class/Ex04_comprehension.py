"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컨프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컨프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컨프리핸션
        { 표현식 for 표현식 in 순회가능객체 }

"""
import random

# 컨프리핸션 사용하지 않은 리스트 생성
alist = []
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.append(6)
print(alist)

alist = []
for n in range(1, 6):
    alist.append(n)
print(alist)

alist = list(range(1, 6))
print(alist)

print("------------------------------------------------")
# 리스트 컨프리핸션
bList = [i for i in range(1, 6)]
print(bList)

bList = [i - 1
         for i in range(1, 6)]
print(bList)

bList = [i * 2
         for i in range(1, 6)]
print(bList)

bList = [i
         for i in range(1, 6)
         if i % 2 == 1]
print(bList)

rows = range(1, 4)
cols = range(1, 3)
arr = [(r, c)
       for r in rows
       for c in cols]  ##type Tuple
print(arr)

for r, c in arr:
    print(r, c)
print("------------------------------------------------")
# 딕셔러니 컨프리핸션
a = {x: x ** 2  ## value
     for x
     in (2, 3, 4)}  ## key
print(a)
##Output count characters at word in string(create dictionary)
word = "Hello World"
## l : 3
## o : 2
cntWord = {letter: word.count(letter)
           for letter
           in word}
print(cntWord)
print(cntWord.get("l"))

print("------------------------------------------------")
# 셋 컨프리핸션
aset = {i
        for i
        in range(1, 10)
        if i % 2 == 1}
print(aset)
print("------------------------------------------------")
# [참고] 제너레이터 컨프리핸션
# ( ) 를 사용하면 튜플이라 생각하지만 튜플은 컨프리핸션이 없다.
# lotto = random.randint(1,46)
# lotto = [i
#          for i
#          in range(1, 46)]
lotto = [i
         for i
         in range(1,7)
         ]
print(lotto)
for i in range(len(lotto)):
    num = random.randint(1, 45)
    lotto[i] = num
lotto.sort()
print(lotto)
