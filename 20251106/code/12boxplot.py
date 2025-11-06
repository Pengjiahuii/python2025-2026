import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def boxplot_api():
    """
    箱线图完整API示例
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    np.random.seed(42)
    # 生成三组数据
    data1 = np.random.normal(100, 10, 200)
    data2 = np.random.normal(90, 20, 200)
    data3 = np.random.normal(110, 15, 200)
    data = [data1, data2, data3]
    labels = ['组A', '组B', '组C']

    # boxplot() 方法完整参数
    boxplot = ax.boxplot(data,
                         labels=labels,           # 组标签
                         notch=True,              # 显示缺口
                         bootstrap=1000,          # 置信区间计算次数
                         widths=0.6,              # 箱体宽度
                         patch_artist=True,       # 填充颜色
                         showmeans=True,          # 显示均值
                         meanline=True,           # 均值线
                         showfliers=True,         # 显示离群点
                         boxprops=dict(alpha=0.7),  # 箱体属性
                         medianprops=dict(color='red', linewidth=2),  # 中位数线属性
                         meanprops=dict(color='green', linewidth=2),  # 均值线属性
                         flierprops=dict(marker='o', color='red', alpha=0.5),  # 离群点属性
                         capprops=dict(color='black'),  # 须线帽属性
                         whiskerprops=dict(color='black'))  # 须线属性

    # 自定义颜色
    colors = ['lightblue', 'lightgreen', 'pink']
    for patch, color in zip(boxplot['boxes'], colors):
        patch.set_facecolor(color)

    ax.set_ylabel('数值')
    ax.set_title('箱线图 API 演示')
    ax.grid(True, alpha=0.3)
    plt.show()

boxplot_api()