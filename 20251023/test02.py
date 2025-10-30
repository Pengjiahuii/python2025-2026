import numpy as np

arr = np.random.randint(0, 21, size=100)

print("原始数组：")
print(arr)

result = arr[arr > 10]

print("\n大于 10 的元素：")
print(result)
