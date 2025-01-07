## rule
##  check random in 1~100
import random
from _datetime import datetime, date
from operator import index
from time import process_time_ns

# num = random.randint(1, 100)
# print(num)
# count = 0
# answer = []
#
# for i in range(1, 101):
#     answer.append(i)
# ans_Count = int(len(answer) / 2)
# # print(answer[0:ans_Count])
# hint = ""
# while (1):
#     sum = 0
#     for i in answer:
#         sum += int(answer[i-1])
#
#     count += 1
#
#     x = int(input("Num : "))
#
#     if sum/2 < num:
#         del (answer[0:ans_Count + 1])
#         hint = f"{answer[0]}~{answer[len(answer)-1]}"
#     else:
#         del (answer[ans_Count:len(answer)+1])
#         hint = f"{answer[0]}~{answer[len(answer)-1]}"
#     if x == num:
#             print(f"True, Now Count is {count}")
#             print(hint)
#             break
#     else:
#             print(f"False, Now Count is {count}")
#             print(hint)
#

## mynumber info
myNumberList = []
count = 0
while (1):

    num = random.randint(0, 9)
    myNumberList.append(num)
    if count == 2 and num > 1:
        del myNumberList[count]
        continue

    elif count == 4 and num > 4:
        del myNumberList[count]
        continue

    elif count == 6:
        if num == 0 or num > 4:
            del myNumberList[count]
            continue

    count += 1
    if len(myNumberList) == 13:
        break
print(myNumberList)
myNumber = ""

for k, v in enumerate(myNumberList):
    myNumber += str(v)
    if k == 5:
        myNumber += "-"
print(myNumber)

## (1)sex output
sex = myNumberList[6]
if sex == 1 or sex == 3:
    print(f"male")
elif sex == 2 or sex == 4:
    print(f"female")
## (2)age
today = date.today()
if myNumberList[6] == 1 or 2:
    age = today.year - (int(myNumberList[0] * 10 + int(myNumberList[1])) + 1900)
else:
    age = today.year - (int(myNumberList[0] * 10 + int(myNumberList[1])) + 2000)
print(age)
## (birth place : 8num)

# 0 = 서울
# 1 = 인천/경기
# 3, 4 = 충청도
# 5 = 전라도
# 7, 8 = 경상도
# 9 = 제주도

print()
str = 'HELLO'  # 문자열
li = ['a', 'b', 'c']  # 리스트
tpl = ('ㄱ', 'ㄴ', 'ㄷ')  # 튜플
di = dict(k=5, j=6)  # 딕셔너리

## unpacking : take to pieces each element
c1, c2, c3 = li
print(c1)
print(c2)
print(c3)
print()
for k, v in di.items():
    print(f"k : {k}")
    print(f"v : {v}")
print()
## If case Tuple to element of list
alist = [(1,2), (3,4), (5,6)]
d1, d2, d3 = alist
print(d1)
for k, v in alist:
    print(f"{k} + {v} = {k+v}")

## round sequences
days = ["월", "화", "수"]
doIt = ["sleep", "study", "eat"]
print(zip(days, doIt)) ##return memory address
print(list(zip(days, doIt)))
print(dict(zip(days, doIt))) ## zip(key, value)
for d, do in zip(days, doIt):
    print(d, do)