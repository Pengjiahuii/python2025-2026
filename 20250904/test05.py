sum_even = 0
for i in range(2, 101, 2):
    sum_even += i
print("1~100偶数和(for):", sum_even)

sum_even = 0
i = 2
while i <= 100:
    sum_even += i
    i += 2
print("1~100偶数和(while):", sum_even)

