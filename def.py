def say():
    return 'Hi'

# a = say()
# print(a)

def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))
    return a + b

# print(add(23, 42))

def say():
    print('Hi')

def sub(a, b):
    return a - b
result = sub(10, 3)

# -- 이렇게도 가능
# result = sub(b=5, a=3)
# print(result)

# 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# result = add_many(1, 2, 3)
# print(result)

# result = add_many()
# print(result) # None ? 0? 

def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result

# result = add_mul('add', 1, 2, 3, 4, 5)
# print(result)
# result = add_mul('mul', 1, 2, 3, 4, 5)
# print(result)

# 키워드 매개변수, keyword arguments
def print_kwargs(**kwargs):
    print(kwargs["name"])

# print_kwargs(name = 'foo', age = 3)

# 함수의 리턴 값
def add_and_mul(a, b):
    return a + b, a * b

# result = add_and_mul(3, 4)
# print(result)

result1, result2 = add_and_mul(3, 4) 

def say_nick(nick):
    if nick == '바보':
        return
    print("나의 별명으니 %s입니다." % nick)

def say_myself(name, age, man = True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
# say_myself("박응용1", 27)
# say_myself("박응용", 27, True)

# 초기 값이 있는 매개변수는 뒤에 위치해야한다.
# def say_myself(name, man = True, age): 

# a = 1
# b = 100

# def vartest(a):
#     a += 1
#     return a
# a = vartest(a)
# print(a)

# def vartest(a):
#     a += 1
#     b = 50
#     c = 100
#     return a + b + c

# result = vartest(a)
# print(result)

a = 1
def vartest():
    global a
    a += 1

vartest()
print(a)

# 람다
add 