def is_odd(number):
    if number % 2 == 1:
        return True
    else: 
        return False
    
# print(is_odd(3))
# print(is_odd(11))

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

# print(avg_numbers(1, 2))
# print(avg_numbers(1, 2, 3, 4, 5))

# 숫자 하나를 받아서 n단을 출력하는 함수 만들기
def a(num):
    for i in range(1, 10):
        print(num, "*", i, "=", num * i)
a(3)