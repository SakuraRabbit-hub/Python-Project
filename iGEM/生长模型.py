import numpy as np

"""
分析：当生长所需资源只能支撑某个最大限度的种群数量，而不能支持种群数量的无限增长，当接近这个最大值时，种群数量的增长速度就会慢下来
①以Δp来表征增长速度
②Δp与当前种群数p(n)有关
③Δp与剩余资源有关，而剩余资源用（种群最大值和当前种群数的差值）来表征，初始资源用种群最大值表征
使用递归模型：Δp = p(n-1) - p(n) = k * (种群最大值-p(n)) * pn
"""
# 导入实验数据
pn = [5,18,29,47,71,119,174,257,350,441,513,559,594,629,640,651,655,659]
deltap = [13,11,18,24,48,55,83,93,91,72,46,35,35,11,11,4,4,2]
pn = np.array(pn)
factor = pn*(663-pn) # 663为观测到的种群极限数值
f = np.polyfit(factor, deltap, 1) #polyfit多项式拟合，其中factor是拟合函数，deltap为自变量，1代表一阶拟合
print(f) #求出f里的k和b
# 至此得出模型：Δp = p(n-1) - p(n) = 8.04286925e-04 * (663-p(n)) * pn

# 画图
import matplotlib.pyplot as plt
time = [i for i in range(0,19)]
p0 = 5
p_list = []
for i in range(19):
    p_list.append(p0)
    p0 = 8.04286925e-04 * (663-p0) * p0 + p0
plt.title('model') # 创建标题
plt.xlabel('time') # x轴
plt.ylabel('number') # y轴
plt.plot(time, p_list) # 画图
plt.show()