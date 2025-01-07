import random

# 10부터 1씩 감소하여 출력
num = []
count = 0
for i in range(1, 11):
    num.append(i)
num.reverse()
print(num)

string = ""
x = len(num)
for i in range(x):
    string += f"{x}, "
    x -= 1
    if x == 1:
        string += f"{x}"
        break
print(string)

# 수를 입력받아 다음 결과로 출력
star = ""
for i in range(1, 6):
    star += "*"
    print(star)

# 로또
lotto = []
while (1):
    num = random.randint(1, 45)
    if num not in lotto:
        lotto.append(num)
    if len(lotto) == 6:
        break

lotto.sort()

while (1):
    bonus = random.randint(1, 45)
    if bonus not in lotto:
        lotto.append(bonus)
        break

print(lotto)
