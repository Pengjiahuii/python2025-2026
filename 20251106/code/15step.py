import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def step_plot_api():
    """
    阶梯图API示例
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.arange(10)
    y = np.random.randint(1, 10, 10)

    # step() 方法 - 不同的阶梯样式
    ax.step(x, y,
            where='pre',        # 阶梯位置：'pre', 'post', 'mid'
            label='pre',
            linewidth=2)

    ax.step(x, y + 2,
            where='post',
            label='post',
            linewidth=2)

    ax.step(x, y + 4,
            where='mid',
            label='mid',
            linewidth=2)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('阶梯图 API 演示')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.show()

step_plot_api()