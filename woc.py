# 인스턴스 생성시 2개의 숫자를 지정
# 지정된 숫자로 4칙 연산 (덧셈, 뺄셈, 곱셈, 나누기)을 수행하는 메서드 구현s
# 위 내용을 테스트 할 수 있는 코드 구현 (인스턴스 생성, 메서드 실행)
# 위 클래스를 상속받아, 제곱 기능을 추가하는 클래스 생성 및 테스트
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
print("덧셈:", calc.add())
print("뺄셈:", calc.subtract())
print("곱셈:", calc.multiply())
print("나눗셈:", calc.divide()) 

# Calculator를 상속받아 제곱 기능 추가
class PowerCalculator(Calculator):
    def power(self):
        return self.num1 ** self.num2

# PowerCalculator 클래스 테스트
power_calc = PowerCalculator(2, 3)
print("제곱:", power_calc.power())  