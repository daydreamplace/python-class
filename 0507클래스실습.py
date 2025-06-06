## 1번. 아래 실습 코드 1에 있는 클래스를 상속하여 값을 뺄 수 있는 minus 메서드를 추가하라
# 생성할 클래스 명: UpgradeCalculator
class Calculator():
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

# 2번. 아래 실습 코드 1에 있는 클래스를 상속하여 객체 변수 value가 100 이상의 값을 가질 수 없도록 제한하는 클래스를 만들어 보시오.
# 생성할 클래스 명: MaxLimitCalculator

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

# 3번. 대학 학사관리 시스템을 개발하는 중이다. 아래의 기능이 포함되도록 클래스를 구현하시오.
# 관리 대상정보 (객체변수) : 이름, 학번, 학년, 전공, 수강과목 및 학점 (딕셔너리 형태)
# 구현기능(메서드): 수강과목 및 학점 추가 / 삭제, 학점 변경, 수강과목의 학점 조회
class Student:
    def __init__(self, name, student_id, year, major, subjects):
        self.name = name
        self.univCode = ''
        self.grade = 0
        self.major = ''
        self.score = {}

    def addScore(self, subject, grade):
        self.score[subject] = grade
    
    def delScore(self, subject):
        pass

    def modScore(self, subject, grade):
        pass
    
    def viewScore(self, subject):
        pass

