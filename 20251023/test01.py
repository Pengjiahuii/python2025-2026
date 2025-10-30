import numpy as np
arr = np.random.randint(1, 11, size=(5, 5))
print("原始数组：")
print(arr)

max_value = arr.max()
arr[arr == max_value] = 0
print("\n最大值替换为0后的数组：")
print(arr)
