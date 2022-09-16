# 需求：画出某城市11点到12点这1小时内每分钟的温度变化折线图，温度范围在15-18℃
import matplotlib.pyplot as plt
plt.rc('font', family='SimHei', size=7)
import random

# 1） 准备数据x, y
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]

# 2） 创建画布
plt.figure(figsize=(20, 8), dpi=80)

# 3） 绘制图像
plt.plot(x, y_shanghai)

    # 修改x, y刻度
x_label = ["11点{}分".format(i) for i in x]
plt.xticks(x[::5], x_label[::5])
plt.yticks(range(0, 40, 5))
    # 添加网格显示
plt.grid(True, linestyle='--', alpha= 0.5)
    # 添加描述信息
plt.xlabel("时间变化")
plt.ylabel("温度")
plt.title("某城市温度变化图")

# 4） 显示图像
plt.show()