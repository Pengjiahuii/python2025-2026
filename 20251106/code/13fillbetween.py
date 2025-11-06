import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def area_plot_api():
    """
    面积图API示例
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # 基础面积图
    ax.fill_between(x, y1,
                    alpha=0.3,           # 透明度
                    color='blue',        # 颜色
                    label='sin(x)')      # 图例标签

    # 两个曲线之间的面积
    ax.fill_between(x, y1, y2,
                    where=(y1 > y2),     # 填充条件
                    alpha=0.5,
                    color='red',
                    label='sin(x) > cos(x)')

    ax.fill_between(x, y1, y2,
                    where=(y1 <= y2),
                    alpha=0.5,
                    color='green',
                    label='sin(x) <= cos(x)')

    ax.plot(x, y1, 'b-', linewidth=2)
    ax.plot(x, y2, 'r-', linewidth=2)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('面积图 API 演示')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.show()

area_plot_api()