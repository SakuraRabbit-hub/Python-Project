import numpy as np
import random
import matplotlib.pyplot as plt

# 设置二维生长区域(200 * 200)
length = 200
width = 200

# 创建生长区域矩阵
cell = np.zeros((length, width), int)
cell_temp = np.asarray(cell)

# 0代表无细胞，1代表细胞
# 初始化矩阵：底层全为细胞
cell_temp[199, :] = 1


# 一直寄的规则区
n = 0
while n < 20:
    # 通过读取cell矩阵，判断每个元胞是存活还是死亡，将结果保存在cell_temp中，最终再复制给cell
    cell = np.array(cell_temp)
    # 显示每一轮的图像
    plt.imshow(cell)
    plt.pause(0.2)

    # 两重循环遍历整个矩阵，判断每个元胞的下一个状态
    for i in range(1, length - 1):
        for j in range(1, width - 1):

            pk = 0.6
            # 如果一个单元格是1，且上方单元格为0，则以pk概率分裂到上方元胞
            if (cell[i][j] == 1 and cell[i + 1], [j] == 0):
                cell_temp[i + 1][j] = pk
                continue
    np.where(cell_temp >= 0.5, 1, 0)

    n += 1