import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def scatter_plot_api():
    """
    散点图完整API示例
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    np.random.seed(42)
    x = np.random.randn(100)
    y = np.random.randn(100)
    sizes = np.random.randint(10, 200, 100)
    colors = np.random.rand(100)

    # scatter() 方法完整参数
    scatter = ax.scatter(x, y,
                         s=sizes,           # 点的大小
                         c=colors,          # 点的颜色
                         marker='o',        # 点形状
                         alpha=0.6,         # 透明度
                         cmap='viridis',    # 颜色映射
                         edgecolors='black', # 边缘颜色
                         linewidths=0.5,    # 边缘宽度
                         label='数据点')     # 图例标签

    # 添加颜色条
    plt.colorbar(scatter, ax=ax, label='颜色值')

    ax.set_xlabel('X 值')
    ax.set_ylabel('Y 值')
    ax.set_title('散点图 API 演示')
    ax.legend()
    plt.show()

scatter_plot_api()