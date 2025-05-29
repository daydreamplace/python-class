# 기본 사용법
import numpy

arr = numpy.array([1, 2, 3, 4, 5])
# print(arr) # [1 2 3 4 5]

# 이름 지정하기!
import numpy as np
arr = np.array((1, 2, 3, 4, 5))
# print(arr) # [1 2 3 4 5]
# print(type(arr)) # <class 'numpy.ndarray'>  # numpy.ndarray는 다차원 배열을 지원하는 객체

# 배열의 차원
import numpy as np

arr0 = np.array(42) # 0차원 배열
arr1 = np.array([1, 2, 3, 4, 5]) # 1차원 배열
arr2 = np.array([[1, 2, 3], [4, 5, 6]]) # 2차원 배열
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # 3차원 배열

# print(arr0.ndim) # 0차원 # dimension = dim = 차원
# print(arr1.ndim) # 1차원 (배열)
# print(arr2.ndim) # 2차원 (배열 안에 배열)
# print(arr3.ndim) # 3차원 (배열 안에 배열 안에 배열)
# 데이터 관점에서 차원이란 데이터의 구조를 의미한다. 

# 
# import numpy as np
# arr = np.array([1, 2, 3, 4], ndim = 5)
# print(arr)
# print(arr.ndim) # 5차원

import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, 1:4]) # [7 8 9] # 1행 1열부터 4열까지
# print(arr[0:2, 2])

arr2 = np.array(['apple', 'banana', 'cherry'])
# print(arr2[0]) # apple

arr1 = np.array([1, 2, 3, 4], dtype = "S")
arr2 = np.array([1, 2, 3, 4], dtype = "i4")
# print(arr1.dtype)
# print(arr2.dtype)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()

# print(x.base) # None
# print(y.base) # [1 2 3 4 5]

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) # 1차원에서 2차원으로 재구성
newarr2 = arr.reshape(2, 3, 2) # 1차원에서 3차원으로 재구성
# print(newarr2)


# x = [1, 2, 3, 4]
# y = [4, 5, 6, 7]
# z = np.add(x, y)
# print(z)

# add() 함수 사용 예시
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
# print(newarr)

# subtract() 함수 사용 예시
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)
# print(newarr)

# multiply() 함수 사용 예시
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.multiply(arr1, arr2)
# print(newarr)

# divide() 함수 사용 예시
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
newarr = np.divide(arr1, arr2)
# print(newarr)

# power() 함수 사용 예시
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])
newarr = np.power(arr1, arr2)
# print(newarr)

# mod() 함수 사용 예시
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.mod(arr1, arr2)
# print(newarr)

# remainder() 함수 사용 예시
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.remainder(arr1, arr2)
# print(newarr)

# divmod() 함수 사용 예시
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.divmod(arr1, arr2)
# print(newarr)

# absolute() 함수 사용 예시
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
# print(newarr)

# abs() 함수 사용 예시
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
# print(newarr) 

# trunc() 함수 사용 예시
arr = np.trunc([-3.1666, 3.6667])
# print(arr)

# around() 함수 사용 예시
arr = np.around(3.1666, 2)
# print(arr)

# floor() 함수 사용 예시
arr = np.floor([-3.1666, 3.6667])
# print(arr)

# ceil() 함수 사용 예시
arr = np.ceil([-3.1666, 3.6667])
# print(arr)

# logs
arr = np.arange(1, 10)
# print(np.log2(arr))

# log2() 함수 사용 예시
arr = np.arange(1, 10)
# print(np.log10(arr))

# log e
arr = np.arange(1, 10)
# print(np.log(arr))


# 
from math import log
nplog = np.frompyfunc(log, 2, 1)
# print(nplog(100, 15))

# product() 함수 사용 예시
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
# print(newarr)

# diff() 함수 사용 예시
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n = 2)
# print(newarr)

# lcm
num1 = 4
num2 = 6
x = np.lcm(num1, num2)

# print(x) 

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
# print(x)

arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
# print(x) 

# gcd()
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
# print(x)

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)