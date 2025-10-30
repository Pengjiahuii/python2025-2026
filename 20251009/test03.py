def calculator():
    try:
        a = float(input("请输入第一个数字："))
        b = float(input("请输入第二个数字："))
        op = input("请输入运算符（+ - * /）：").strip()

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b
        else:
            print("错误：不支持的运算符！")
            return

    except ValueError:
        print("错误：输入的不是有效数字，请输入浮点数或整数。")
    except ZeroDivisionError:
        print("错误：除数不能为0。")
    except Exception as e:
        print(f"未知错误：{e}")
    else:
        print(f"计算结果：{a} {op} {b} = {result}")
    finally:
        print("程序执行完毕。")

calculator()
