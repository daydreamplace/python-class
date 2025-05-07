test = abs(3) # 절대값
test = abs(-1.2)

test = all([1,2,3]) # 모두 True인지 확인
test = all([1,2,3,0]) # 0이 들어가면 False
test = all([])

test = any([1,2,3]) # 하나라도 True면 True
test = any([0, "", [], False]) # 모두 False면 False
test = any([])


test = chr(97) # 아스키코드 97에 해당하는 문자
test = chr(44032) # 아스키코드 44032에 해당하는 문자

test = dir([1,2,3]) # 객체의 속성이나 메서드 확인
test = dir({'1':'a'})

test = divmod(7, 3) # 몫과 나머지를 튜플로 반환
# print(7 // 3)
# print(7 % 3)

for i, name in enumerate(['a', 'b', 'c']):
    print(i, name) # 인덱스와 값을 함께 출력

eval('1 + 2')
eval("'hi' + 'a'")
eval('divmod(4, 3)')
print(test)

