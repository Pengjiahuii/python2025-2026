import matplotlib.pyplot as plt
# import numpy as np

# # 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def basic_plotting_framework():
    """
    Matplotlib 基础绘图框架 - 7个标准步骤
    """

    # 步骤1：导入必要的库
    #import matplotlib.pyplot as plt
    import numpy as np

    # 步骤2：准备数据
    x = np.linspace(0, 10, 100)  # 生成0到10的100个等间距点
    y1 = np.sin(x)               # 正弦函数
    y2 = np.cos(x)               # 余弦函数

    # 步骤3：创建图形和坐标轴对象
    fig, ax = plt.subplots(figsize=(10, 6))  # 创建图形和坐标轴

    # 步骤4：绘制图形（核心绘图操作）
    line1 = ax.plot(x, y1, label='sin(x)', color='blue', linewidth=2)
    line2 = ax.plot(x, y2, label='cos(x)', color='red', linewidth=2, linestyle='--')

    # 步骤5：自定义图形样式和布局
    ax.set_title('三角函数图像', fontsize=16, fontweight='bold')  # 设置标题
    ax.set_xlabel('X轴', fontsize=12)                            # X轴标签
    ax.set_ylabel('Y轴', fontsize=12)                            # Y轴标签
    ax.legend(loc='upper right')                                 # 显示图例
    ax.grid(True, alpha=0.3)                                    # 显示网格

    # 步骤6：调整图形细节
    ax.set_xlim(0, 10)                    # 设置X轴范围
    ax.set_ylim(-1.5, 1.5)                # 设置Y轴范围
    plt.tight_layout()                    # 自动调整布局

    # 步骤7：显示或保存图形
    plt.savefig('plot_example.png', dpi=300, bbox_inches='tight')  # 保存图形
    plt.show()                           # 显示图形

# 执行示例
basic_plotting_framework()