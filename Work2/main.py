import numpy as np
import os

# 导入模块
from module1_data import create_grade_matrix, basic_statistics
from module2_student import student_statistics, filter_students, sort_students
from module3_analysis import grade_distribution_analysis, class_overall_analysis
from module4_visual_report import visualize_grades, generate_report
from module5_interactive import query_student


def main():
    print("=== 学生成绩分析系统 ===")

    # --------------------
    # 数据来源选择
    # --------------------
    choice = input("选择数据来源: 1-随机生成, 2-从CSV文件读取: ").strip()

    grades = None
    subjects = None
    student_names = None

    if choice == '2':
        file_path = input("请输入CSV文件路径: ").strip()
        if not os.path.exists(file_path):
            print("文件不存在，使用随机生成成绩代替")
            choice = '1'
        else:
            # 从 CSV 读取
            import csv
            subjects = ['数学', '物理', '化学', '英语', '历史']
            with open(file_path, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # 跳过表头
                data = list(reader)
            student_names = [row[1] for row in data]
            grades = np.array([list(map(int, row[2:])) for row in data])

    if choice != '2':
        try:
            n_students = int(input("请输入学生数量(默认30): ") or 30)
        except:
            n_students = 30
        grades, subjects = create_grade_matrix(n_students=n_students)
        student_names = [f"学生{i + 1}" for i in range(grades.shape[0])]

    # --------------------
    # 基本统计
    # --------------------
    subject_means, subject_max, subject_min, subject_std = basic_statistics(grades, subjects)

    # 学生统计
    student_means, student_totals, student_max, student_min = student_statistics(grades)

    # --------------------
    # 筛选与排序
    # --------------------
    high_achievers, failed_students, all_good = filter_students(grades, student_means, student_totals)
    sorted_by_mean, sorted_by_total, sorted_by_total_math = sort_students(grades, student_means, student_totals)

    print("\n按总分+数学成绩排序前5名学生:")
    for idx in sorted_by_total_math[:5]:
        print(
            f" {student_names[idx]} - 总分: {student_totals[idx]}, 平均分: {student_means[idx]:.1f}, 数学: {grades[idx, 0]}")

    # --------------------
    # 进阶分析
    # --------------------
    grade_levels, correlation_matrix = grade_distribution_analysis(grades, subjects)
    class_mean, class_std, score_ranges, most_variable_idx = class_overall_analysis(grades, student_means)

    # --------------------
    # 可视化
    # --------------------
    visualize_grades(grades, subjects, student_means, class_mean, correlation_matrix, subject_means)

    # --------------------
    # 报告生成
    # --------------------
    generate_report(grades, subjects, student_means, student_totals, subject_means)

    # --------------------
    # 交互式查询
    # --------------------
    query_student(grades, subjects, student_names)


if __name__ == "__main__":
    main()
