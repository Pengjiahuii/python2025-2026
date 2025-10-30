def process_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

            numbers = [int(line.strip()) for line in content.split('\n') if line.strip()]

    except FileNotFoundError:
        print(f"错误：文件 {filename} 不存在")
        return None
    except ValueError as e:
        print(f"错误：文件包含非数字内容 - {e}")
        return None
    except PermissionError:
        print(f"错误：没有读取文件 {filename} 的权限")
        return None
    except Exception as e:
        print(f"发生未知错误：{e}")
        return None
    else:
        print("文件读取成功")
        return numbers

result = process_file("numbers.txt")
if result is not None:
     print(f"读取到的数字列表：{result}")

