a = b = 'python'

print(a) # 'python'
print(b) # 'python'
print(id(a)) # 4363952960
print(id(b))    # 4363952960

a = 'b'

print(a) # 'b'
print(b) # 'python'
print(id(a)) # 4385515256