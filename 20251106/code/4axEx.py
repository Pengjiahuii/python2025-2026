import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def axes_methods_demo():
    """
    Axes 对象的方法和属性演示
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # 绘图数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # 1. 基本绘图方法
    line, = ax.plot(x, y, label='sin(x)')  # 返回Line2D对象

    # 2. 坐标轴设置方法
    ax.set_xlabel('X轴标签', fontsize=12)          # 设置X轴标签
    ax.set_ylabel('Y轴标签', fontsize=12)          # 设置Y轴标签
    ax.set_title('坐标轴标题', fontsize=14)         # 设置标题
    ax.set_xlim(0, 10)                            # 设置X轴范围
    ax.set_ylim(-1.5, 1.5)                        # 设置Y轴范围

    # 3. 刻度和网格设置
    ax.set_xticks(np.arange(0, 11, 2))            # 设置X轴刻度位置
    ax.set_xticklabels(['零', '二', '四', '六', '八', '十'])  # 设置刻度标签
    ax.grid(True, linestyle='--', alpha=0.5)      # 显示网格

    # 4. 图例和注释
    ax.legend(loc='upper right')                  # 显示图例
    ax.annotate('最大值', xy=(np.pi/2, 1), xytext=(4, 1.2),
                arrowprops=dict(arrowstyle='->'))  # 添加注释

    # 5. 文本和形状
    ax.text(5, 0, '中心点', ha='center', va='center',
            fontsize=12, color='red')             # 添加文本
    ax.axhline(y=0, color='green', linestyle='--')  # 添加水平线
    ax.axvline(x=5, color='gray', linestyle='-')  # 添加垂直线

    # 6. 获取和设置属性
    print(f"X轴范围: {ax.get_xlim()}")            # 获取X轴范围
    print(f"Y轴范围: {ax.get_ylim()}")            # 获取Y轴范围
    print(f"标题: {ax.get_title()}")              # 获取标题

    plt.tight_layout()
    plt.show()

# 执行示例
axes_methods_demo()