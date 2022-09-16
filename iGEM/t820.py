import numpy as np
import random
import matplotlib.pyplot as plt
import random

# 设置三维生长区域(200 * 200 *200)
height = 20
length = 20
width = 20
# 设置相关参数
rate = 0.3

# 创建生长区域矩阵
cell = np.zeros((length, width, height), int)
cell_temp = np.array(cell)
# 初始化矩阵，0代表无细胞，1代表有细胞
cell_temp[:, 19, :] = 1


# 函数区

# 扩增函数
def amp(cell, i, j, k, amp_rate):
    # 判断是否超出边界
    i_list = [i - 1, i, i + 1]
    i_del = []
    j_list = [j - 1, j, j + 1]
    j_del = []
    k_list = [k - 1, k, k + 1]
    k_del = []

    for i_n in i_list:
        try:
            a = cell[i_n, 0, 0]
        except IndexError:
            i_del.append(i_n)
    for i_n in i_del:
        i_list.remove(i_n)

    for j_n in j_list:
        try:
            a = cell[0, j, 0]
        except IndexError:
            j_del.append(j_n)
    for j_n in j_del:
        j_list.remove(j_n)

    for k_n in k_list:
        try:
            a = cell[0, 0, k_n]
        except IndexError:
            k_del.append(k_n)
    for k_n in k_del:
        k_list.remove(k_n)

    amp_rate_t = 1
    for i_n in i_list:
        for j_n in j_list:
            for k_n in k_list:
                if i == i_n and j == j_n and k == k_n:
                    continue
                if cell[i_n][j_n][k_n] == 1:
                    amp_rate_t = amp_rate_t * (1 - amp_rate)
    rate = random.uniform(0, 1)
    if (1 - rate) <= amp_rate_t:
        return 1
    else:
        return 0


# 绘制三维等高线图
def con(cell, x, y):
    con = np.zeros((length, width))
    for j in range(length):
        for k in range(width):
            num = 0
            for i in range(0, height):
                if cell[i][j][k] == 0:
                    num += 1
                else:
                    break
                con[j][k] = height - 1 - num
    return con


# 规则区
n = 0
while n < 3:
    # 通过读取cell矩阵，判断每个元胞是存活还是死亡，将结果保存在cell_temp中，最终再复制给cell    
    cell = np.array(cell_temp)
    # 显示每一轮的图像
    # plt.imshow(cell)
    # plt.pause(o.2)
    # 三重循环遍历整个矩阵，判断每个元胞的下一个状态
    for i in range(0, height):
        for j in range(0, length):
            for k in range(0, width):
                if cell[i][j][k] == 0:
                    cell_temp[i][j][k] = amp(cell, i, j, k, rate)
    x = np.linspace(0, length, length)
    y = np.linspace(0, width, width)
    X, Y = np.meshgrid(x, y)
    Z = con(cell_temp, x, y)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, Z, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # 调整观察角度和方位角。这里将俯仰角设为60度，把方位角调整为35度
    ax.view_init(60, 35)
    plt.pause(0.2)
    n += 1
