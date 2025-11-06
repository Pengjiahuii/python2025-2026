import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def bar_plot_api():
    """
    柱状图完整API示例
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    categories = ['产品A', '产品B', '产品C', '产品D', '产品E']
    values1 = [23, 45, 56, 12, 41]
    values2 = [34, 30, 45, 23, 38]

    x = np.arange(len(categories))
    width = 0.35

    # bar() 方法完整参数
    bars1 = ax.bar(x - width/2, values1, width,
                   color='skyblue',        # 柱状图颜色
                   edgecolor='navy',       # 边缘颜色
                   linewidth=1,            # 边缘宽度
                   alpha=0.8,              # 透明度
                   label='2022年',         # 图例标签
                   hatch='/',              # 填充图案：'/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'
                   align='center',         # 对齐方式：'center', 'edge'
                   yerr=[2, 3, 1, 4, 2],  # 误差线
                   capsize=5)              # 误差线帽大小

    bars2 = ax.bar(x + width/2, values2, width,
                   color='lightcoral',
                   edgecolor='darkred',
                   label='2023年')

    # 添加数值标签
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height}', ha='center', va='bottom')

    ax.set_xlabel('产品类别')
    ax.set_ylabel('销量')
    ax.set_title('柱状图 API 演示')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    plt.show()

bar_plot_api()