import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def figure_methods_demo():
    """
    Figure 对象的方法和属性演示
    """
    # 创建Figure对象
    fig = plt.figure(
        figsize=(8, 6),      # 图形大小（宽，高）英寸
        dpi=100,             # 分辨率
        facecolor='white',   # 背景颜色
        edgecolor='black',   # 边框颜色
        linewidth=1,         # 边框宽度
        frameon=True,        # 是否显示边框
        layout='tight'       # 布局引擎
    )

    # 关键属性
    print(f"图形大小: {fig.get_size_inches()}")      # 获取图形尺寸
    print(f"DPI: {fig.dpi}")                        # 获取分辨率
    print(f"图形编号: {fig.number}")                 # 图形编号

    # 关键方法
    ax1 = fig.add_subplot(211)                      # 添加子图 2行1列第1个
    ax2 = fig.add_subplot(212)                      # 添加子图 2行1列第2个

    # 在子图中绘图
    x = np.linspace(0, 10, 100)
    ax1.plot(x, np.sin(x))
    ax2.plot(x, np.cos(x))

    # Figure级别的方法
    fig.suptitle('Figure总标题', fontsize=14)        # 设置总标题
    fig.tight_layout()                              # 自动调整布局
    fig.savefig('figure_demo.png', dpi=300)         # 保存图形
    fig.show()                                      # 显示图形

    plt.close(fig)  # 关闭图形释放内存

# 执行示例
figure_methods_demo()