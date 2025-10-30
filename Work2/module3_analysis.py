import numpy as np

def grade_distribution_analysis(grades, subjects):
    """成绩等级分布和相关性分析"""
    grade_levels = np.full(grades.shape, 'F', dtype='<U1')
    grade_levels[grades >= 60] = 'D'
    grade_levels[grades >= 70] = 'C'
    grade_levels[grades >= 80] = 'B'
    grade_levels[grades >= 90] = 'A'
    correlation_matrix = np.corrcoef(grades, rowvar=False)
    return grade_levels, correlation_matrix

def class_overall_analysis(grades, student_means):
    class_mean = np.mean(student_means)
    class_std = np.std(student_means)
    score_ranges = {
        '优秀': np.sum(student_means >= 90),
        '良好': np.sum((student_means >= 80) & (student_means < 90)),
        '中等': np.sum((student_means >= 70) & (student_means < 80)),
        '及格': np.sum((student_means >= 60) & (student_means < 70)),
        '不及格': np.sum(student_means < 60)
    }
    most_variable_idx = np.argmax(grades.std(axis=1))
    return class_mean, class_std, score_ranges, most_variable_idx
