import args


def test(t):
    t = 20
    print ("In Function:", t)
x = 10
print ("Before:", x)
test(x)
print ("After:", x)

def sotring_function(list_value):
    return list_value.sort()

print(sotring_function([5,4,3,2,1]))

def is_yes(your_answer):
    if your_answer.upper() == "YES" or your_answer.upper() == "Y":
        result = your_answer.lower()
print(is_yes("Yes"))

def add_and_mul(a, b, c):
    return b + a * c + b
print(add_and_mul(3, 4, 5) == 63)

# def args_test_3(one, two, *args, three):
#     print(one + two + sum(args))
#     print(args)
# args_test_3(3, 4, 5, 6, 7)

def rain(colors):
    colors.append("purple")
    colors = ["green", "blue"]
    return colors
rainbow = ["red", "orange"]
print(rain(rainbow))


def function(value):
    print(value ** 3)
print(function(2))

def get_apple(fruit):
    fruit = list(fruit)
    fruit.append("e")
    fruit = ["apple"]
    return fruit
fruit = "appl"
get_apple(fruit)
print(fruit)

def return_sentence(sentence, n):
    sentence += str(n)
    n -= 1
    if n < 0:
        return sentence
    else:
        return(return_sentence(sentence, n))
sentence = "I Love You"
print(return_sentence(sentence, 5))


def test(x, y):
    tmp = x
    x = y
    y = tmp
    return y.append(x)

x = ["y"]
y = ["x"]
test(x, y)
print(y)


def factorial_calculator(n):
    if n in (0, 1):
        return 1

    return n * factorial_calculator(n-1)
print(factorial_calculator(5))

l = [1,2,3,4]
y = [[5],[6]]
l = y
print(y)