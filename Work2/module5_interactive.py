import numpy as np

def query_student(grades, subjects, student_names):
    """
    交互式查询学生成绩
    grades: np.ndarray，学生成绩矩阵
    subjects: list，科目名称
    student_names: list，学生姓名
    """
    print("\n=== 学生成绩查询系统 ===")
    while True:
        name = input("请输入学生姓名（输入 exit 退出）: ")
        if name.lower() == "exit":
            print("退出查询系统。")
            break
        if name in student_names:
            idx = student_names.index(name)
            print(f"\n学生 {name} 的成绩如下：")
            for i, sub in enumerate(subjects):
                print(f"  {sub}: {grades[idx, i]}")
            total = np.sum(grades[idx])
            avg = np.mean(grades[idx])
            print(f"  总分: {total}, 平均分: {avg:.2f}\n")
        else:
            print("未找到该学生，请重新输入。\n")
