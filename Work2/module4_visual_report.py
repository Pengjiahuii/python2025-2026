import matplotlib.pyplot as plt
import numpy as np

# ---------- 中文字体设置 ----------
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题
# ----------------------------------

def visualize_grades(grades, subjects, student_means, class_mean, correlation_matrix, subject_means):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    axes[0, 0].bar(subjects, subject_means, color='skyblue', alpha=0.7)
    axes[0, 0].set_title('各科目平均分')

    axes[0, 1].hist(student_means, bins=15, color='lightgreen', edgecolor='black')
    axes[0, 1].axvline(class_mean, color='red', linestyle='--', label=f'班级平均: {class_mean:.1f}')
    axes[0, 1].set_title('学生平均分分布')
    axes[0, 1].legend()

    axes[1, 0].boxplot(grades, labels=subjects)
    axes[1, 0].set_title('各科目成绩箱线图')

    im = axes[1, 1].imshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1)
    axes[1, 1].set_title('科目相关性热力图')
    axes[1, 1].set_xticks(range(len(subjects)))
    axes[1, 1].set_yticks(range(len(subjects)))
    axes[1, 1].set_xticklabels(subjects)
    axes[1, 1].set_yticklabels(subjects)
    for i in range(len(subjects)):
        for j in range(len(subjects)):
            axes[1, 1].text(j, i, f'{correlation_matrix[i, j]:.2f}', ha='center', va='center')
    plt.colorbar(im, ax=axes[1, 1])
    plt.tight_layout()
    plt.show()


def generate_report(grades, subjects, student_means, student_totals, subject_means):
    n_students, n_subjects = grades.shape
    print(f"分析对象: {n_students}名学生, {n_subjects}门科目")
    print(
        f"班级平均分: {np.mean(student_means):.2f}, 班级最高分: {np.max(student_means):.2f}, 最低分: {np.min(student_means):.2f}")
    best_subject_idx = np.argmax(subject_means)
    print(f"平均分最高科目: {subjects[best_subject_idx]} ({subject_means[best_subject_idx]:.2f})")
