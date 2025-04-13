# 그냥 리스트
# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

# 리스트 안의 튜플
# a =[(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first + last)

marks = [90, 25, 67, 45, 80]

# number = 0
# for mark in marks:
#     number += 1
#     if mark >= 60:
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

# number = 0
# for mark in marks:
#     number += 1
#     if mark >= 60:
#         continue
#     print("%d번 학생은 합격입니다." % number)

a = range(10)
# print(a)

# for i in a:
#     print(i)

# 1부터 100까지 더하기
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)

# 3의 배수
# for i in range(1, 101):
#     if i % 3 == 0:
#         print(i)

# for와 range를 이용한 구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print("%d x %d = %d" % (i, j, i * j))

# 3단 부터
# for i in range(3, 6):
#     for j in range(1, 10):
#         print("%d x %d = %d" % (i, j, i * j))

# 리스트 컴프리헨션
# a = [1, 2, 3, 4]
# result = []
# for num in a:
#     result.append(num * 3)
# print(result)

# result = [x * y for x in range(2, 10) for y in range(1, 10)]
# print(result)
