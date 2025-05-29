from numpy import random

# x = random.rand()

# x1 = random.randint(100, size=(5))
# x2 = random.randint(100, size= (3,5))

# print(x)
# print(x1)
# print(x2)

x = random.choice([3, 5, 7, 9])
print(x)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

arr2 = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr2))
print(arr2)