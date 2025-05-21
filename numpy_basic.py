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

