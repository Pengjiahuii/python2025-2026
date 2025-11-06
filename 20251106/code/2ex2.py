import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def advanced_subplot_framework():
    """
    高级多子图绘图框架
    """

    # 步骤1：创建多子图布局
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))  # 2x2子图网格
    fig.suptitle('多子图示例', fontsize=16, fontweight='bold')  # 总标题

    # 生成示例数据
    x = np.linspace(0, 10, 50)
    y1 = np.sin(x)
    y2 = np.cos(x)
    categories = ['A', 'B', 'C', 'D']
    values = [25, 40, 30, 35]

    # 步骤2：在各个子图中绘制不同的图形
    # 子图1：折线图
    axes[0, 0].plot(x, y1, 'b-', label='sin(x)')
    axes[0, 0].plot(x, y2, 'r--', label='cos(x)')
    axes[0, 0].set_title('折线图')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # 子图2：散点图
    axes[0, 1].scatter(x, y1 + np.random.normal(0, 0.1, len(x)),
                       alpha=0.6, color='green', s=30)
    axes[0, 1].set_title('散点图')
    axes[0, 1].grid(True, alpha=0.3)

    # 子图3：柱状图
    axes[1, 0].bar(categories, values, color='skyblue', alpha=0.7)
    axes[1, 0].set_title('柱状图')

    # 子图4：饼图
    axes[1, 1].pie(values, labels=categories, autopct='%1.1f%%')
    axes[1, 1].set_title('饼图')

    # 步骤3：统一调整布局
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)  # 为总标题留出空间

    # 步骤4：保存和显示
    plt.savefig('subplot_example.png', dpi=300, bbox_inches='tight')
    plt.show()

# 执行示例
advanced_subplot_framework()