# 列表创建示例
# list1 = ['beijing','shanghai','guangzhou','shenzhen']
# list2 = []                          # 创建空列表
# list3 = list((1,3,5,7,9))           # 由元组转换为列表
# list4 = list(range(1, 10, 2))       # [1,3,5,7,9]
# list5 = list("hello")               # ['h','e','l','l','o']

# 列表添加
# list1 = [1,2,3,4]
# list1.append(5)                     # 结果: [1,2,3,4,5]
# list1.extend([6,7,8])               # 结果: [1,2,3,4,5,6,7,8]
# list1.insert(3, 10)                 # 在索引3插入10

# 列表相乘（注意引用问题）
# list2 = [1,2,3]
# list2 = list2 * 3                   # [1,2,3,1,2,3,1,2,3]
# list3 = [[None] * 2] * 3            # 注意：会产生浅复制的引用
# list3[0][0] = 10                    # 会影响所有子列表

# 列表合并（+ 会生成新列表，成本较高）
# list1 = [1,2,3,4]
# new_list = list1 + [5]              # [1,2,3,4,5]

# 列表删除操作
# list1 = [1,3,5,7,9]
# del list1[2]                        # 结果: [1,3,7,9]
# x = list1.pop()                     # 弹出并返回最后一个元素
# x = list1.pop(2)                    # 弹出并返回索引2的元素
# list2 = [1,3,5,3,7]
# list2.remove(3)                     # 删除第一次出现的3

# 访问与修改
# list1 = [2,4,6,8]
# x = list1[0]                        # x=2
# list1[1] = 10                       # 结果: [2,10,6,8]
# # 注意索引越界会抛出 IndexError

# 查找与判断
# pos = list1.index(6)                # 返回6的索引，找不到会抛异常
# exists = 6 in list1                 # True / False

# 切片示例（超出范围安全）
# a = list(range(10))                 # [0,1,2,3,4,5,6,7,8,9]
# a[:5]                               # [0,1,2,3,4]
# a[1:6]                              # [1,2,3,4,5]
# a[::2]                              # [0,2,4,6,8]
# a[6:100]                            # [6,7,8,9]

# 基于切片修改
# list1 = [1,3,5,7,9]
# list1[:3] = [10,20,30]              # [10,20,30,7,9]
# list1[:2] = []                      # 删除前2个
# del list1[:2]                       # 删除切片
# list1[len(list1):] = [11]           # 在尾部追加元素11

# 浅复制与深复制
# list1 = [1,3,5,7]
# list2 = list1[:]                     # 浅复制，基本类型安全
# import copy
# list3 = [1, [3], 5, 7]
# list4 = list3[:]                      # 浅复制，内层列表共享引用
# list5 = copy.deepcopy(list3)          # 深复制，完全独立

# 排序与反转
# list1 = [10,25,5,36,80,68]
# list1.sort()                          # 原地升序
# list1.sort(reverse=True)              # 原地降序
# list2 = sorted(list1)                 # 返回新列表
# list1.reverse()                       # 原地逆序
# list3 = list(reversed(list1))         # 返回新逆序列表

# 自定义排序示例
# words = ['banana','apple','cherry','date']
# words.sort(key=len)                   # 按字符串长度排序
# data = [{'name':'Alice','age':30},{'name':'Bob','age':25}]
# data.sort(key=lambda x: x['age'])     # 按字典键 age 排序
# data.sort(key=lambda x: (x['age'], x['name']))  # 多条件排序

# 列表推导式与生成器表达式
# list1 = [x*x for x in range(5)]       # [0,1,4,9,16]
# flat = [num for sub in [[1,2],[3,4]] for num in sub]  # 展平嵌套列表
# positives = [i for i in [2,-10,9,4.6,-2,0] if i > 0]   # 过滤正数
# gen = (i*i for i in range(5))         # 生成器表达式，消耗一次

# 使用海象运算符示例
# values = [y for x in range(10) if (y := x * 2) > 5]   # [6,8,10,12,14,16,18]

# 统计示例
# scores = [80,76,92,85,62,56,98,78]
# highest = max(scores)
# lowest = min(scores)
# average = sum(scores) / len(scores)

# enumerate 用法
# fruits = ['apple','banana','cherry']
# for index, fruit in enumerate(fruits, start=1):
#     print(index, fruit)

# zip 用法示例
# keys = ['广东','山东','河南']
# values = [126012510,101527453,99365519]
# for k,v in zip(keys, values):
#     print(k, v)

# starred expression 示例（拆包剩余元素）
# car_prices = [50,26,14,80,150,10,5,30]
# car_prices_desc = sorted(car_prices, reverse=True)
# highest, *others, lowest = car_prices_desc

# 列表与元组内存占用示例
# list1 = [1,2,3]
# tuple1 = (1,2,3)
# print('Size of list:', list1.__sizeof__())
# print('Size of tuple:', tuple1.__sizeof__())

# 元组示例与解包
# tuple1 = ('shanghai', 2024, 6341)
# city, year, area = tuple1

# 字典创建与常用操作
# dict1 = {'AI':'artificial intelligence', 'DL':'deep learning'}
# dict2 = {}
# keys = ['name','gender','age']
# values = ['Li Ming','male',16]
# dict3 = dict(zip(keys, values))
# dict4 = dict(name='Li Ming', age=16)
# dict1['age'] = 17
# dict1['phone'] = '13812345678'
# dict1.update({'a':5, 'd':6})    # 合并字典

# 字典安全访问
# value = dict1.get('c', 'default_value')
# if 'c' in dict1:
#     value = dict1['c']
# value = dict1.setdefault('c', 'default_value')

# 字典推导示例
# newd = {n: n*2 for n in range(3)}

# 集合创建与操作
# letters = {'a','b','c','d'}
# my_set = set([1.0, 'hello', (1,2,3)])
# set1 = set('hello')
# set1.add('q')
# set1.update({1,2,3}, {'x','y'})
# elem = set1.pop()
# set1.clear()
# set1.discard(3)    # 不存在不会抛出
# # set1.remove(4)   # 不存在会抛异常

# 从列表去重
# list1 = [1,2,3,2,3,'Finance','computer','Finance']
# list2 = list(set(list1))

#实用函数示例（等额本金还款计算）
# def calculate_monthly_payments_equal_principal(principal, annual_interest_rate, loan_years):
#     """计算等额本金每月还款金额，返回每月还款金额列表。"""
#     number_of_payments = loan_years * 12
#     monthly_interest_rate = annual_interest_rate / 12.0
#     monthly_principal = principal / number_of_payments
#     monthly_payments = []
#     remaining_principal = principal
#     for i in range(number_of_payments):
#         monthly_interest = remaining_principal * monthly_interest_rate
#         monthly_payments.append(monthly_principal + monthly_interest)
#         remaining_principal -= monthly_principal
#     return monthly_payments
#

# 投资组合蒙特卡洛示例
# import random
# def portfolio_optimization(returns, risks, num_portfolios=10000):
#     """简单蒙特卡洛：按最大(期望回报/风险)比选择权重。"""
#     num_assets = len(returns)
#     best_score = -1.0
#     best_weights = None
#     for _ in range(num_portfolios):
#         weights = [random.random() for _ in range(num_assets)]
#         total = sum(weights)
#         weights = [w/total for w in weights]
#         port_return = sum(w * r for w, r in zip(weights, returns))
#         port_risk = sum(w * s for w, s in zip(weights, risks))
#         if port_risk == 0:
#             continue
#         score = port_return / port_risk
#         if score > best_score:
#             best_score = score
#             best_weights = weights
#     return best_weights


# 学生-课程选课系统示例
# students = ["xiaozhang", "xiaowang", "xiaoli", "xiaozhao"]
# courses = ["Math", "Physics", "Chemistry", "Biology"]
# registration = {
#     "xiaozhang": {"Math", "Physics"},
#     "xiaowang": {"Math", "Chemistry"},
#     "xiaoli": {"Physics", "Biology"},
#     "xiaozhao": {"Math", "Biology", "Chemistry"}
# }
#
# def register_course(student, course):
#     """学生选课"""
#     if student in registration:
#         registration[student].add(course)
#     else:
#         registration[student] = {course}
#     print(f"{student} has successfully registered for {course}.")
#
# def drop_course(student, course):
#     """学生退课"""
#     if student in registration and course in registration[student]:
#         registration[student].remove(course)
#         print(f"{student} has successfully dropped {course}.")
#     else:
#         print(f"{student} is not registered for {course} or {course} does not exist.")
#
# def get_registered_courses(student):
#     """查询学生已选课程"""
#     return registration.get(student, set())
#
# def course_registration_count():
#     """统计每门课的注册人数"""
#     course_count = {}
#     for courses in registration.values():
#         for course in courses:
#             course_count[course] = course_count.get(course, 0) + 1
#     return course_count
#

