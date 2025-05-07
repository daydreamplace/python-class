class FourCal:
    # 생성자 메서드
    # __init__ 메서드는 클래스가 인스턴스화 될 때 자동으로 호출되는 메서드
    # 클래스 첫 인수 self 중요
    # self는 인스턴스 자신을 가리키는 변수
    # 첫번째로 받을 값이 first, 두번째로 받을 값이 second
    def __init__(self, first, second):
        self.first = first
        self.second = second
    # 더하기 메서드
    def add(self):
        result = self.first + self.second
        return result
    # 빼기 메서드
    def sub(self):
        result = self.first - self.second
        return result
    # 곱하기 메서드
    def mul(self):
        result = self.first * self.second
        return result
    # 나누기 메서드
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
b = FourCal(8, 3)

# 밖에서도 바꿀 수 있음
# a.first = 2
# a.first -= 2
b.second -= 1

# print(a.first)
# print(a.add())
# print(b.add())
# print(b.sub())


# 상속
# 새 클래스를 생성하지만 FourCal 클래스를 상속받음
class MoreFourCal(FourCal):
    # 이미 FourCal 클래스에 정의된 div를 덮어쓴다. 이를 오버라이딩이라고 함!
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
    # 제곱
    def pow(self):
        result = self.first ** self.second
        return result


# 인스턴스 생성
a = MoreFourCal(4, 2)
# 
b = FourCal(4, 2)

# print(a.first)
# print(a.div())
# print(a.pow())
# print(b.pow()) # FourCal에는 pow 메서드 없어서 에러 발생


# 오버라이딩 메서드 사용해보기
a = MoreFourCal(4, 0)
print(a.div())

b = FourCal(4, 0)
print(b.div())