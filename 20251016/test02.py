class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我的名字叫{self.name}，{self.age}岁了")

p1 = Person("彭佳辉", 20)
p1.introduce()
