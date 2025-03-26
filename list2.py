a = [1,2,3]
print(a[1]) # 2
print(a[0] + a[2]) # 4
print(a[-1]) # 3


b = [1,2,3, ["a", "b", "c"]]
print(b[3][0]) # a

c = [1,2,3,4,5]
print(a[0:2]) # [1,2] 앞에꺼는 포함 뒤는 불포함
print(a[:2]) 

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]

d = a[1:3] # 앞에꺼는 포함 뒤는 불포함
print(d) # [2, 3]


e = [1,2,3]
f = [4,5,6]
g = e * 3
# h = e + "20"
len(e)
print(e)
print(g)

a = [1,2,3]
a.pop(1)
print(a)