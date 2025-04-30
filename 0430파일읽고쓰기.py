### 파일 읽기
# f = open("new-file.txt", "w")
# f.close()

# 1번부터 10번까지의 숫자를 파일에 저장하기
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)

# 파일을 닫아야 저장됨
# f.close()

### 파일 한줄씩 읽기
# f = open("new-file.txt", "r")
# line = f.readline()
# print(line)
# f.close()


### 파일 한줄씩 읽기
# f = open("new-file.txt", "r")
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

### 파일 전체 읽기 (리스트 형태로 나옴)
# f = open("new-file.txt", "r")
# lines = f.readlines()

# for line in lines:
#     line = line.strip() # 줄바꿈 문자 제거
#     print(line)
# f.close()

### 파일 전체 내용을 리턴
# f = open("new-file.txt", "r")
# data = f.read()
# print(data)
# f.close()

### 1줄씩 읽기
# f = open("new-file.txt", "r")
# for line in f:
#     print(line)
# f.close()

### 파일에 새로운 내용 추가하기
f = open("new-file.txt", "a")
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
