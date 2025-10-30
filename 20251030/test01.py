import pandas as pd
import numpy as np

courses = ['数学', '英语', '计算机', '物理', '化学', '生物', '历史', '地理', '政治', '体育']

彭佳辉 = pd.Series(np.random.randint(0, 101, size=10), index=courses)

print("彭佳辉的成绩：")
print(彭佳辉)

print("\n平均分：", 彭佳辉.mean())
print("最高分：", 彭佳辉.max())
print("最低分：", 彭佳辉.min())

print("\n不及格课程：")
print(彭佳辉[彭佳辉 < 60])
