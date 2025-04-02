# money = 2000
# card = True

# if money >= 3000 or card:
#     print("택시를")
#     print("타고")
#     print("가라")
# else:
#     print("걸어가라")

# pocket = ['paper', 'cellphone', 'money']

# if 'money' in pocket:
#     print("택시를")
#     print("타고")
#     print("가라")
# else:
#     print("걸어가라")

# if '0000money' in pocket:
#     print("택시를")
#     print("타고")
#     print("가라")
# else:
#     print("걸어가라")

# # pass가 있으면 넘어감
# if 'money' in pocket:
#     pass
# else:
#     print("걸어가라")

# pocket = ['paper', 'cellphone']
# card = True

# if 'money' in pocket:
#     print("택시를 타고 가라 1")
# else:
#     if card:
#         print("택시를 타고 가라 2")
#     else:
#         print("걸어가라")

# if 'money' in pocket:
#     print("택시를 타고 가라 1")
# elif card:
#     print("택시를 타고 가라 2")
# else:
#     print("걸어가라")

score = 80
message = ""

# if score <= 60:
#     message = "success"
# else:
#     message = "failure"
# print(message)

# 삼항연산자.....????
message = "success" if score <= 60 else "failure"
# 다른 언어에서 사용하는 삼항연산자
# score <= 60 ? "success" : "failure"