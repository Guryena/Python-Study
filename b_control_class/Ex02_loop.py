# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""


a = 112  # 숫자형
b = ['1', '2', '3']  # 리스트
c = '987'  # 문자열
d = tuple(b)  # 튜플
e = dict(k=5, j=6)  # 딕셔너리

# for entry in a: # a는 반복이 안되지만 b부터 e까지는 반복된다.
#    print(entry)
try:
    for i in a:
        print(i)
except:
    print("Do not")

for i in b:
    print(i)
print()

for i in c:
    print(i)
print()

for i in d:
    print(i)
print()

for i in e:
    print(i)
print()

for i in e.values():
    print(i)
print()

for i in e.items():
    print(i)
print()

"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
Mul = []
for i in range(2, 10):
    listMul = []
    for j in range(1, 10):
        mul = i * j
        listMul.append(mul)
        print(f"{i} x {j} = {mul}")
    Mul.append(listMul)
print(Mul)

sum = 0
for i in range(1, 11, 2):
    sum += i
print(sum)
print()

sum = 0
for i in range(1, 11):
    if i % 2 == 1:
        sum += i
print(sum)
print()


def mul(x):
    result = []
    for i in range(1, 10):
        mul = x * i
        result.append(f"{x} x {i} = {mul}")
    return result


def mulString(x):
    for i in range(1, 10):
        mul = x * i
        print(f"{x} x {i} = {mul}")


while (True):
    try:
        x = int(input("Number : "))
        break
    except:
        continue

print(mul(x))
mulString(x)
print()

# =========================================================
# while

# a = 1
# while True:  # 무한루프
#    if a == 1:
#        print(a)
#        break
sum = 0
i = 0
while (1):
    if i <= 10:
        sum += i
        i += 1
    else:
        break
print(sum)
print()

a = ["z", "y", "x"]
while a:
    data = a.pop(-1)
    print(data)
    if data == "y":
        break
print()

