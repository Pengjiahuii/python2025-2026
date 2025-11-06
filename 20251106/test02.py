import matplotlib.pyplot as plt
import pandas as pd

# 设置中文字体和负号正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False

# 示例数据：每天花费（可替换为你的完整数据）
dates = pd.date_range(start="2025-11-01", periods=10)
expenses = [10.5, 8.2, 12.0, 6.5, 9.8, 11.2, 7.5, 13.0, 10.0, 8.7]

# 计算3日移动平均
moving_avg = pd.Series(expenses).rolling(window=3).mean()

# 创建图表
plt.figure(figsize=(12,6))

# 柱状图
plt.bar(dates, expenses, color='skyblue', label='每日花费')

# 折线图
plt.plot(dates, expenses, color='orange', marker='o', label='折线花费')

# 移动平均线
plt.plot(dates, moving_avg, color='red', linestyle='--', label='3日移动平均')

# 高低花费标记
for i, val in enumerate(expenses):
    if val >= 12:
        plt.scatter(dates[i], val, color='red', s=100, zorder=5)
    elif val <= 7:
        plt.scatter(dates[i], val, color='green', s=100, zorder=5)

# 添加标题和坐标轴标签
plt.title('每日花费可视化', fontsize=16)
plt.xlabel('日期', fontsize=12)
plt.ylabel('花费（元）', fontsize=12)

# 美化
plt.xticks(rotation=45)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# 保存为图片
plt.savefig("每日花费可视化.png", dpi=300)

print("图表已保存为每日花费可视化.png")
