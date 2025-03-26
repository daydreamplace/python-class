t1 = (1)
print(t1)

print(type(t1)) # <class 'int'>

t1 = (1,)
print(t1)

t1 = (1, 2, 'a', 'b')
print(t1[1]) # 2

# del t1[1]
print(t1) # TypeError: 'tuple' object doesn't support item deletion
# 튜플은 한번 생성하면 그 값을 변경할 수 없다. 따라서 튜플의 요소를 삭제하거나 변경하려고 하면 에러가 발생한다.

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
print(t3)

print(t1[0:3]) # (1, 2, 'a')

