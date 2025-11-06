import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体支持（解决中文显示问题）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def pie_chart_api():
    """
    饼图完整API示例
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    sizes = [30, 25, 20, 15, 10]
    labels = ['技术部', '销售部', '市场部', '人事部', '财务部']
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange']
    explode = (0.1, 0, 0, 0, 0)  # 突出显示第一部分

    # pie() 方法完整参数
    wedges, texts, autotexts = ax.pie(sizes,
                                      explode=explode,        # 突出部分
                                      labels=labels,          # 标签
                                      colors=colors,          # 颜色
                                      autopct='%1.1f%%',      # 百分比格式
                                      shadow=True,            # 阴影
                                      startangle=90,          # 起始角度
                                      radius=1.0,             # 半径
                                      counterclock=False,     # 顺时针
                                      wedgeprops={'edgecolor': 'black', 'linewidth': 1},  # 楔形属性
                                      textprops={'fontsize': 12},  # 文本属性
                                      center=(0, 0),          # 中心位置
                                      frame=False)            # 是否显示框架

    # 美化百分比文本
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')

    ax.set_title('公司部门分布 - 饼图 API 演示')
    plt.show()

pie_chart_api()