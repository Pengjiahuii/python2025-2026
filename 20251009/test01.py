def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "错误：除数不能为0"
    except TypeError:
        return "错误：输入的参数类型不正确"

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, "2"))
