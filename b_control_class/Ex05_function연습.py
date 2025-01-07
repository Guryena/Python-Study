import random


# [ 연습문제 ]
# - 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수 ( 함수명 : even_filter )
def even_filter(x):
    num = []
    for i in x:
        if i % 2 == 0:
            num.append(i)
    return num


#     [ 출력 결과 ]
print(even_filter([1, 2, 4, 5, 8, 9, 10]))
print()


# - 주어진 수가 소수인지 아닌지 판단하는 함수 ( 함수명 : is_prime_number )
def is_prime_number(x):
    num = []
    for i in range(2, x + 1):
        num.append(i)
    for j in range(2, len(num)):
        for k in range(2, len(num)):
            if j * k in num:
                num.remove(j * k)
    if num[-1] == x:
        return f"{x} is prime number"
    else:
        return f"{x} is not prime number"


#     [ 출력 결과 ]
print(is_prime_number(60))
print(is_prime_number(61))
print()


# - 주어진 문자열에서 모음의 개수를 출력하는 함수 ( 함수명 : count_vowel )
def count_vowel(str):
    strList = list(str)
    vowel = ["a", "e", "i", "o", "u", "y"]
    vowelList = []
    count = 0
    for i in strList:
        if i in vowel:
            vowelList.append(i)
    print(vowelList)
    return len(vowelList)


#     [ 출력 결과 ]
print(count_vowel("pythonian"))


def lottery(x):
    inputNum = input(f"Number : ")
    numList = list(f"{x:02d}")
    inputList = list(inputNum)
    for i in range(len(inputList)):
        for j in range(len(numList)):
            if numList == inputList:
                return "1등"
            elif numList[i] == inputList[i] or numList[j] == inputList[j]:
                return "2등"
        return "False"


def lottery1():
    inputNum = input(f"Number : ")
    number = random.randint(1, 99)
    print(number)
    numList = list(f"{number:02d}")
    inputList = list(inputNum)

    for i in range(len(inputList)):
        for j in range(len(numList)):
            if numList == inputList:
                return "1st"
            elif numList[i] == inputList[i] or numList[j] == inputList[j]:
                return "2nd"

        return "False"


# number = random.randint(1, 99)
# print(number)
# result = lottery(number)
# print(result)
# result1 = lottery1()
# print(result1)


# 1. 문자열을 입력받아 모든 문자를 대문자로 변환하여 반환하는 함수를 생성하고 호출
def getString(x):
    upper = x.upper()
    return upper


print(getString("sadfasdfaf adfasdfasf"))


# 2. 가로/세로 길이를 입력받아 넓이를 구하는 함수
def get_area(x, y):
    area = x * y
    return area


print('넓이 : ', get_area(4, 5))  # 넓이 : 20 출력
print()


# 3. 리스트 형태의 값을 받아 처리하는 함수
# 호출 예)
# fruit = ['orange', 'mango', 'apple']
# 1) get_fruit(fruit)         # 리스트의 모든 과일 [목록/갯수]가 출력됨
# 2) print(isfruit('mango'))    # True 출력
# 3) print(isfruit('Grapefruit '))    # False 출력
def get_fruit(fruit):
    dicf = {}

    for i in fruit:
        dicf[i] = fruit.count(i)

    for j in dicf:
        print(f"{j} : {dicf.get(j)}")


def isfruit(value):
    if value in fruitList:
        return True
    else:
        return False


fruitList = ['orange', 'mango', 'apple', 'orange']
get_fruit(fruitList)
print(isfruit('mango'))  # True 출력
print(isfruit('Grapefruit '))  # False 출력
