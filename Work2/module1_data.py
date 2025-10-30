import numpy as np


def create_grade_matrix(n_students=30, n_subjects=5, from_file=None):
    """
    创建学生成绩矩阵
    from_file: 如果提供CSV文件路径，则从文件读取，否则随机生成
    """
    subjects = ['数学', '物理', '化学', '英语', '历史']

    if from_file:
        data = np.loadtxt(from_file, delimiter=',', skiprows=1)
        grades = data[:, 1:]  # 假设第一列是学号
        print(f"从文件 {from_file} 读取成绩数据，形状: {grades.shape}")
    else:
        np.random.seed(42)
        grades = np.random.randint(60, 101, (n_students, n_subjects))
        print(f"随机生成成绩矩阵，形状: {grades.shape}")

    return grades, subjects


def basic_statistics(grades, subjects):
    """计算各科目基本统计量"""
    subject_means = grades.mean(axis=0)
    subject_max = grades.max(axis=0)
    subject_min = grades.min(axis=0)
    subject_std = grades.std(axis=0)
    return subject_means, subject_max, subject_min, subject_std
