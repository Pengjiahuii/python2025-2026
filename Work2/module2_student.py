import numpy as np


def student_statistics(grades):
    """计算学生个人统计量"""
    print("\n=== 学生个人统计 ===")

    # 每个学生平均分
    student_means = np.mean(grades, axis=1)
    # 每个学生总分
    student_totals = np.sum(grades, axis=1)
    # 每个学生最高分和最低分
    student_max = np.max(grades, axis=1)
    student_min = np.min(grades, axis=1)

    # 打印前10个学生的统计
    for i in range(min(10, grades.shape[0])):
        print(
            f"学生{i + 1}: 平均分={student_means[i]:.1f}, 总分={student_totals[i]}, 最高={student_max[i]}, 最低={student_min[i]}")

    return student_means, student_totals, student_max, student_min


def filter_students(grades, student_means, student_totals):
    """基于条件的筛选"""
    print("\n=== 条件筛选 ===")

    # 平均分≥90
    high_achievers = np.where(student_means >= 90)[0]
    print("平均分≥90的学生索引:", high_achievers)

    # 有科目不及格(<60)
    failed_students = np.where(np.min(grades, axis=1) < 60)[0]
    print("有科目不及格的学生索引:", failed_students)

    # 所有科目都≥80
    all_good = np.where(np.min(grades, axis=1) >= 80)[0]
    print("所有科目≥80的学生索引:", all_good)

    return high_achievers, failed_students, all_good


def sort_students(grades, student_means, student_totals):
    """对学生进行排序"""
    print("\n=== 学生排序 ===")

    # 按平均分降序
    sorted_by_mean = np.argsort(-student_means)
    print("按平均分降序索引前5:", sorted_by_mean[:5])

    # 按总分降序
    sorted_by_total = np.argsort(-student_totals)
    print("按总分降序索引前5:", sorted_by_total[:5])

    # 按总分+数学成绩排序
    # 数学成绩在第0列
    sorted_by_total_math = np.lexsort((-grades[:, 0], -student_totals))
    print("按总分+数学成绩排序前5:", sorted_by_total_math[:5])

    return sorted_by_mean, sorted_by_total, sorted_by_total_math
