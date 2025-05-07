class Family:
    lastname = "김"

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

# 모델에 바로 접근해서 바꾸기
Family.lastname = '박'

# 클래스 변수에 접근해서 바꾸기
a.lastname = '이'

print(a.lastname)
print(b.lastname)