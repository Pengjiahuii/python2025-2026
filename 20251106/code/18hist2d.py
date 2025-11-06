import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号


def hist2d_api():
    """
    二维直方图API示例
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    np.random.seed(42)
    x = np.random.normal(0, 1, 1000)
    y = np.random.normal(0, 1, 1000)

    # hist2d() 方法
    h = ax.hist2d(x, y,
                  bins=30,              # 箱子数量
                  range=[[-3, 3], [-3, 3]],  # 数据范围
                  cmap='hot',           # 颜色映射
                  density=True)         # 显示密度

    # 添加颜色条
    plt.colorbar(h[3], ax=ax, label='密度')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('二维直方图 API 演示')
    plt.show()

hist2d_api()