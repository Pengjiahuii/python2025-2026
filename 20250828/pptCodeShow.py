s="Hello World!我是彭佳辉。"
print("s1:", s)

"Hello, {}. You are {} years old.".format("Alice", 30)
print("s2:", "Hello, {}. You are {} years old.".format("Alice", 30))

print("s3:", '{0}加上{1}等于{2}'.format(10, 20, 10 + 20))

print("s4:", "The number is {:.2f}".format(3.14159))

print("s5:", "Left aligned: {:<10}".format("test"))

print("s6:", "Right aligned: {:>10}".format("test"))

print("s7:", "Center aligned: {:^10}".format("test"))

print("s8:", "Padded: {:*^10}".format("test"))

print("s9:", "Number with commas: {:,}".format(123456789))

print("s10:", "Percentage: {:.2%}".format(0.756))

import datetime
now = datetime.datetime.now()
print("s11:", "Current date: {:%Y-%m-%d %H:%M}".format(now))

print(1+5)
print(5-2)
print(2*6)
print(2**10)
print(1/2)
print(9//4)
print(9%4)
print(1<2)
print(2<=3)
print(1==2)
print(2!=3)

x1, y1 = 1, 2
delta_x, delta_y = 5, 10
x1, y1 = x1 + delta_x, y1 - delta_y
print("s12:", x1, y1)

a = None
if a is None:
    print("s13:", "a is None")

a = 10
b = 10
print("s14:", a is b)
print("s15:", a == b)

a = 1000
b = 1000
print("s16:", a is b)
print("s17:", a == b)

a = [1, 2, 3]
b = [1, 2, 3]
if a is not b:
    print("s18:", "a and b are not the same object")

account_a, account_b = 10000, 10000
interest_rate_a, interest_rate_b = 0.02, 0.1
total_a = account_a * pow((1 + interest_rate_a), 30)
total_b = account_a * pow((1 + interest_rate_b), 30)
print("s19:", "Total asset of A:", round(total_a))
print("s20:", "Total asset of B:", round(total_b))

USD_TO_RMB = 6.5
usd_amount = float(input("请输入要转换的美元数量: "))
rmb_amount = usd_amount * USD_TO_RMB
print("s21:", "{} 美元等于 {:.2f} 人民币".format(usd_amount, rmb_amount))

sales_last_year = float(input("请输入去年的销售额: "))
sales_this_year = float(input("请输入今年的销售额: "))
cost_last_year = float(input("请输入去年的成本: "))
cost_this_year = float(input("请输入今年的成本: "))
profit_last_year = sales_last_year - cost_last_year
profit_this_year = sales_this_year - cost_this_year
profit_margin_last_year = (profit_last_year / sales_last_year) * 100
profit_margin_this_year = (profit_this_year / sales_this_year) * 100
growth_rate = ((sales_this_year - sales_last_year) / sales_last_year) * 100
print("s22:", "去年的利润率为: {:.2f}%".format(profit_margin_last_year))
print("s23:", "今年的利润率为: {:.2f}%".format(profit_margin_this_year))
print("s24:", "销售增长率为: {:.2f}%".format(growth_rate))

