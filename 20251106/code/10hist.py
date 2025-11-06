import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def histogram_api():
    """
    直方图完整API示例
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    np.random.seed(42)
    data1 = np.random.normal(170, 10, 1000)  # 正态分布数据
    data2 = np.random.normal(160, 15, 800)   # 另一组数据

    # hist() 方法完整参数
    n, bins, patches = ax.hist(data1,
                               bins=30,           # 柱子数量或边界
                               range=(140, 200),  # 数据范围
                               density=True,      # 显示密度而非计数
                               color='skyblue',   # 颜色
                               alpha=0.7,         # 透明度
                               edgecolor='black', # 边缘颜色
                               linewidth=0.5,     # 边缘宽度
                               label='组1',       # 图例标签
                               cumulative=False,  # 是否累积
                               histtype='bar',    # 类型：'bar', 'barstacked', 'step', 'stepfilled'
                               orientation='vertical',  # 方向：'vertical', 'horizontal'
                               rwidth=0.8)        # 相对宽度

    # 叠加另一个直方图
    ax.hist(data2, bins=30, density=True, alpha=0.7,
            color='lightcoral', label='组2')

    ax.set_xlabel('数值')
    ax.set_ylabel('密度')
    ax.set_title('直方图 API 演示')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.show()

histogram_api()