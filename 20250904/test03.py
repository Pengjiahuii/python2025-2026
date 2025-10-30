a, b = 0, 1
fib = []

while a <= 1000:
    fib.append(a)
    a, b = b, a + b

# 打印数列
print("斐波那契数列：")
for num in fib:
    print(num, end=" ")
print("\n")

# 打印相邻两项比值（跳过第一个0）
print("相邻两项比值：")
for i in range(2, len(fib)):
    ratio = fib[i] / fib[i-1]
    print(f"{ratio:.4f}", end=" ")
