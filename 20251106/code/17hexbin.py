import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def hexbin_plot_api():
    """
    六边形箱图API示例 - 适用于大数据集
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    np.random.seed(42)
    # 生成大量数据点
    x = np.random.normal(0, 1, 10000)
    y = np.random.normal(0, 1, 10000)

    # hexbin() 方法
    hb = ax.hexbin(x, y,
                   gridsize=30,         # 网格大小
                   cmap='viridis',      # 颜色映射
                   bins='log',          # 统计方式：'log', None
                   mincnt=1,            # 最小计数
                   edgecolors='none',   # 边缘颜色
                   alpha=0.8)           # 透明度

    # 添加颜色条
    cb = fig.colorbar(hb, ax=ax, label='点数')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('六边形箱图 API 演示 - 大数据集可视化')
    plt.show()

hexbin_plot_api()