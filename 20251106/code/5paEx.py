import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def styling_parameters_demo():
    """
    样式参数详细演示
    """
    fig, ax = plt.subplots(figsize=(12, 8))

    x = np.linspace(0, 10, 20)

    # 1. 颜色参数
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown']
    for i, color in enumerate(colors):
        ax.plot(x, x + i, color=color, label=f'color: {color}', linewidth=2)

    # 2. 线型参数
    linestyles = ['-', '--', '-.', ':']
    for i, ls in enumerate(linestyles):
        ax.plot(x, x - i - 2, linestyle=ls, label=f'linestyle: {ls}', linewidth=2)

    # 3. 标记参数
    markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h']
    for i, marker in enumerate(markers[:6]):
        ax.plot(x, x - i - 6, marker=marker, linestyle='',
                label=f'marker: {marker}', markersize=8)

    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_title('Matplotlib 样式参数演示')
    plt.tight_layout()
    plt.show()

# 执行演示
styling_parameters_demo()