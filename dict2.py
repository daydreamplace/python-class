a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1992'}

b = list(a.keys())
b = list(a.values())
b.append("abc")
print(b)

# a.clear() # 딕셔너리 안의 모든 요소를 삭제한다.

print(a)
# print(a['name']) # pey
# print(a['test']) # key가 없으면 에러가 난다.
print(a.get('test')) # key가 없으면 None을 출력한다. like null, undefined

print('name' in a) # True
print('test' in a) # False