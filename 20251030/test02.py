import pandas as pd

scores = pd.read_excel("学生成绩原始表.xlsx", index_col=0)

def calc_gpa(course, score):
    if course == "语文":
        if score < 60:
            return 0
        elif score < 80:
            return 6
        else:
            return 8
    elif course == "数学":
        if score < 60:
            return 0
        elif score < 80:
            return 8
        else:
            return 10
    elif course == "计算机":
        if score < 60:
            return 0
        elif score < 80:
            return 5
        else:
            return 6

# 计算绩点
scores["语文绩点"] = scores["语文"].apply(lambda x: calc_gpa("语文", x))
scores["数学绩点"] = scores["数学"].apply(lambda x: calc_gpa("数学", x))
scores["计算机绩点"] = scores["计算机"].apply(lambda x: calc_gpa("计算机", x))

# 计算平均绩点
scores["平均绩点"] = scores[["语文绩点", "数学绩点", "计算机绩点"]].mean(axis=1)

# 排名
scores["绩点排名"] = scores["平均绩点"].rank(ascending=False, method='dense').astype(int)

top3 = scores.sort_values("平均绩点", ascending=False).head(3)

output_file = "学生成绩与绩点排名.xlsx"
scores.to_excel(output_file, sheet_name="绩点结果")

print("✅ 前三名免推保研名单：\n")
print(top3[["语文", "数学", "计算机", "平均绩点"]])
print(f"\n结果已保存到：{output_file}")
