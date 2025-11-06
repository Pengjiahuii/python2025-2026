import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def contour_plot_api():
    """
    等高线图API示例
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    # 生成数据
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)  # 二维函数

    # contour() 方法 - 线框图
    CS = ax.contour(X, Y, Z,
                    levels=10,          # 等高线数量或具体值
                    colors='black',     # 线颜色
                    linewidths=1)       # 线宽

    # contourf() 方法 - 填充图
    CF = ax.contourf(X, Y, Z,
                     levels=20,         # 填充层次
                     cmap='RdYlBu',     # 颜色映射
                     alpha=0.7)         # 透明度

    # 添加标签
    ax.clabel(CS, inline=True, fontsize=8)

    # 添加颜色条
    plt.colorbar(CF, ax=ax, label='函数值')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('等高线图 API 演示')
    plt.show()

contour_plot_api()