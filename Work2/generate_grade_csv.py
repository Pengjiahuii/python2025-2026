import numpy as np
import csv

np.random.seed(42)

# 学生数量
n_students = 30
subjects = ['数学', '物理', '化学', '英语', '历史']

# 生成学生姓名
names = [f"学生{i+1}" for i in range(n_students)]

# 生成成绩矩阵，带分布特征
grades = np.zeros((n_students, len(subjects)), dtype=int)
grades[:, 0] = np.random.randint(80, 101, n_students)   # 数学偏高
grades[:, 1] = np.random.randint(65, 91, n_students)    # 物理平均
grades[:, 2] = np.random.randint(65, 91, n_students)    # 化学平均
grades[:, 3] = np.random.randint(60, 85, n_students)    # 英语稍低
grades[:, 4] = np.random.randint(60, 101, n_students)   # 历史随机

# 文件名
csv_file = "student_grades_sample.csv"

# 写入 CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # 写入表头
    writer.writerow(['学号', '姓名'] + subjects)
    # 写入数据
    for i in range(n_students):
        row = [i+1, names[i]] + grades[i].tolist()
        writer.writerow(row)

print(f"CSV文件生成成功: {csv_file}")
