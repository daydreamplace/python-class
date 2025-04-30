# a = input()
# print(a)

# number = input("숫자를 입력하세요 : ")

## 사용자에게 입력받는 값은 무조건 문자열로 저장됨
# print(type(number)) # str

## 띄어쓰기 안됨
# print("life" "is" "too short")
## 띄어쓰기 됨
# print("life", "is", "too short")

# 줄바꿔서 출력됨
for i in range(10):
    print(i)
# 한줄로 띄어쓰기 후 출력됨
for i in range(10):
    print(i, end = " ")
# 한줄로 숫자 뒤에 ,붙여서 출력됨
for i in range(10):
    print(i, end = ",")

