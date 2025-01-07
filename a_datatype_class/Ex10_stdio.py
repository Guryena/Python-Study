"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
"""
# name = input("Name : ")
# age = input("Age : ")
# age =  int(age)
# print(f"This name is {name}, Type : {type(name)}")
# print(f"Age is {age}, Type : {type(age)}")
# # print("This name is %s. " %name)
# # print("This name is {0}".format(name))
# print()
# x = "1+2"
# print(x, type(x))
# print(eval(x), type(x))
#
# print()
#----------------------------------
# 단을 입력받아 구구단을 구하기
# for i in range(0,9):
#     for j in range(0, 9):
#         print(i*j)
#     print()
#-----------------------------------------

# print() 함수
print("Hello" "World")
print("Hello", "World")
print("Hello"+"World")


# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0         1      2      3
