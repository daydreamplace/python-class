# Calculator 클래스
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "0으로 나눌 수 없습니다."
        return self.num1 / self.num2

# Calculator 클래스 테스트
calc = Calculator(10, 5)
print("더하기", calc.add())
print("빼기", calc.subtract())
print("곱하기", calc.multiply())
print("나누기", calc.divide())
calc = Calculator(9, 3)
print("더하기", calc.add())
print("빼기", calc.subtract())
print("곱하기", calc.multiply())
print("나누기", calc.divide())

# Calculator를 상속, 제곱 기능 추가
class PowerCalculator(Calculator):
    def power(self):
        return self.num1 ** self.num2

# PowerCalculator 클래스 테스트
power_calc = PowerCalculator(2, 3)
print("제곱", power_calc.power())
power_calc = PowerCalculator(3, 2)
print("제곱", power_calc.power()) 