import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def errorbar_api():
    """
    误差棒图API示例
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.arange(1, 6)
    y = [2, 3, 5, 4, 6]
    y_err = [0.5, 0.4, 0.8, 0.3, 0.7]  # 误差值

    # errorbar() 方法
    ax.errorbar(x, y, yerr=y_err,
                fmt='o',               # 数据点格式
                color='blue',          # 颜色
                ecolor='red',          # 误差棒颜色
                elinewidth=2,          # 误差棒线宽
                capsize=5,             # 误差棒帽大小
                capthick=2,            # 误差棒帽厚度
                barsabove=True,        # 误差棒在数据点上方
                label='测量数据')       # 图例标签

    ax.set_xlabel('实验编号')
    ax.set_ylabel('测量值')
    ax.set_title('误差棒图 API 演示')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.show()

errorbar_api()