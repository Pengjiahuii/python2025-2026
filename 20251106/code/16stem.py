import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def stem_plot_api():
    """
    茎叶图API示例
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.linspace(0, 2 * np.pi, 20)
    y = np.sin(x)

    # stem() 方法
    markerline, stemlines, baseline = ax.stem(x, y,
                                              linefmt='gray',   # 茎线格式
                                              markerfmt='o',    # 标记格式
                                              basefmt=' ',      # 基线格式
                                              bottom=0,         # 基线位置
                                              label='sin(x)')   # 图例标签

    # 自定义样式
    plt.setp(markerline, color='red', markersize=8)
    plt.setp(stemlines, color='blue', linewidth=1)

    ax.set_xlabel('角度')
    ax.set_ylabel('振幅')
    ax.set_title('茎叶图 API 演示')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.show()

stem_plot_api()