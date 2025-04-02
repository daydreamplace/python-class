#  1. 평균점수 구하기
국어 = 80
영어 = 75
수학 = 55
평균 = (국어 + 영어 + 수학) / 3
print(평균)

# 2. 홀수, 짝수 판별하기 

if 13 % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 3. 주민등록번호 다루기
# 생년월일과 나머지 숫자로 나누기
주민등록번호 = "882230-2068234"
print(주민등록번호.split("-"))
# 성별 구분하기
if int(주민등록번호[7]) % 2 == 0:
    print("여성")
else:
    print("남성")

# 4. 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# 5. 리스트 역순 정렬
c = [1, 3, 5, 4, 2]
c.sort(reverse = True)
print(c)

# 6. 리스트 문자열로 만들기
d = ["Life", "is", "too", "short"]
print(" ".join(d))

# 7. 튜플 더하기
print((1, 2, 3) + (4,))

# 8. 딕셔너리 정보 추가
dict = {}
dict['name'] = 'python'
print(dict)
dict['1'] = 'python'
print(dict)
# dict['a'] = python

# 9. 값 추출하기
e = {'A': 90, 'B': 80, 'C': 70}
for v in e.values():
    print(v)

# 10. 리스트에서 중복값 제거
f = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
f = set(f)
print(10, list(f))

# 11. 파이썬의 변수
a = b = [1, 2, 3]
a[1] = 4
print(b) # [1, 4, 3]