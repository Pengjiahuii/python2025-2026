import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def line_plot_api():
    """
    折线图完整API示例
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # plot() 方法完整参数
    line1 = ax.plot(x, y1,
                    color='blue',           # 线条颜色
                    linestyle='-',          # 线型：'-', '--', '-.', ':'
                    linewidth=2,            # 线宽
                    marker='o',             # 标记形状
                    markersize=4,           # 标记大小
                    markerfacecolor='red',  # 标记填充色
                    markeredgecolor='black', # 标记边缘色
                    markeredgewidth=1,      # 标记边缘宽度
                    label='sin(x)',         # 图例标签
                    alpha=0.8,              # 透明度
                    zorder=2)               # 绘制顺序

    line2 = ax.plot(x, y2, 'r--', label='cos(x)')  # 简写格式

    ax.legend()
    ax.set_title('折线图 API 演示')
    plt.show()

line_plot_api()