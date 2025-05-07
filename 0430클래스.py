class Calculator:
    def __init__(self):
        self.result = 0 # result라는 변수에 0을 넣어줌

    def add(self, num): # 파이썬 class는 self를 넣어줘야 함!!
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator() # cal1이라는 변수에 Calculator라는 class를 넣어줌
cal2 = Calculator() # cal2라는 변수에 Calculator라는 class를 넣어줌

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

print(cal1.sub(5))
print(cal1.sub(2))

print(cal2.sub(4))
print(cal2.sub(3))




a = [1, 2, 3, 4]

a.sort() # 오름차순 정렬