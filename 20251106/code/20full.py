import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def comprehensive_demo():
    """
    Matplotlib 综合演示 - 展示各种图形类型
    """
    # 创建2x3的子图布局
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Matplotlib 图形类型综合演示', fontsize=16, fontweight='bold')

    # 生成示例数据
    np.random.seed(42)
    x = np.linspace(0, 10, 50)
    y_line = np.sin(x)
    y_scatter = y_line + np.random.normal(0, 0.1, len(x))
    categories = ['A', 'B', 'C', 'D', 'E']
    values_bar = [25, 40, 30, 35, 20]
    data_hist = np.random.normal(0, 1, 1000)
    sizes_pie = [30, 25, 20, 15, 10]

    # 1. 折线图
    axes[0, 0].plot(x, y_line, 'b-', linewidth=2, label='sin(x)')
    axes[0, 0].set_title('折线图')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # 2. 散点图
    axes[0, 1].scatter(x, y_scatter, alpha=0.6, color='green', s=30)
    axes[0, 1].set_title('散点图')
    axes[0, 1].grid(True, alpha=0.3)

    # 3. 柱状图
    axes[0, 2].bar(categories, values_bar, color='skyblue', alpha=0.7)
    axes[0, 2].set_title('柱状图')

    # 4. 直方图
    axes[1, 0].hist(data_hist, bins=30, color='lightcoral', alpha=0.7, edgecolor='black')
    axes[1, 0].set_title('直方图')
    axes[1, 0].grid(True, alpha=0.3)

    # 5. 饼图
    axes[1, 1].pie(sizes_pie, labels=categories, autopct='%1.1f%%', startangle=90)
    axes[1, 1].set_title('饼图')

    # 6. 箱线图
    data_box = [np.random.normal(0, 1, 100) for _ in range(3)]
    axes[1, 2].boxplot(data_box, labels=['组1', '组2', '组3'], patch_artist=True)
    axes[1, 2].set_title('箱线图')
    axes[1, 2].grid(True, alpha=0.3)

    # 调整布局
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)

    # 保存图形
    plt.savefig('matplotlib_comprehensive_demo.png', dpi=300, bbox_inches='tight')
    plt.show()

# 执行综合演示
comprehensive_demo()