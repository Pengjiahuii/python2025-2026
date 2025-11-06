import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def horizontal_bar_api():
    """
    水平条形图API示例
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    categories = ['Python', 'JavaScript', 'Java', 'C++', 'C#', 'PHP']
    popularity = [85, 72, 65, 55, 50, 45]

    # barh() 方法 - 水平条形图
    bars = ax.barh(categories, popularity,
                   color='lightgreen',
                   edgecolor='darkgreen',
                   height=0.6,            # 条形高度
                   alpha=0.7)

    # 添加数值标签
    for i, (value, bar) in enumerate(zip(popularity, bars)):
        ax.text(value + 1, bar.get_y() + bar.get_height()/2,
                f'{value}%', va='center')

    ax.set_xlabel('流行度 (%)')
    ax.set_title('编程语言流行度 - 水平条形图')
    plt.tight_layout()
    plt.show()

horizontal_bar_api()