import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

plt.rc('font', family='SimHei', size=12)


"""
文物元胞M：位置固定，可以被腐蚀元胞所腐蚀。
腐蚀元胞C：位置随机，可以腐蚀文物元胞。在三维元胞自动机运行的每个时间步长内，可以在上、下、左、右、前、后六个方向随机选择一个来移动
无属性元胞N：即溶液中的水分子，可以被C占据，也可以在C移动时自动填补到此空位
"""
# 10×10的随机矩阵：设C:N=10:90，即腐蚀溶液浓度为10%
# 1代表C，0代表N
A = np.random.choice([0, 1], size=(2, 10, 10), p=[.5, .5])

# 生成文物元胞矩阵，2代表文物元胞M
B = np.zeros([10, 10, 10], int) + 2

# 合并矩阵
universe = np.vstack((A, B))


# 计算周围1元胞数，返回总的R值
def factor_r(i, j, k, universe):
    num = 0
    universe_c = np.zeros([12, 10, 10], int) + 2
    for a in range(i-1, i+2):
        for b in range(j-1, j+2):
            for c in range(k-1, k+2):
                if universe[a][b][c] == 1:
                    num += 1
    if num >= 7:
        universe_c[i][j][k] = 1

    return universe_c[i][j][k]


# 绘制三维等高图
def con(cell):
    con = np.zeros((10, 10))
    for j in range(10):
        for k in range(10):
            num = 0
            for i in range(0, 11):
                con[j][k] = num
                if cell[i][j][k] == 2:
                    num += 1

    return con


# 更新数据的func函数
def updata(universe):
    universe_new = np.copy(universe)
    for i in range(0, 11):
        for j in range(0, 9):
            for k in range(0, 9):
                if universe[i][j][k] == 2:
                    universe_new[i][j][k] = factor_r(i, j, k, universe)

    universe = np.copy(universe_new)

    _x = np.arange(0, 10)
    _y = np.arange(0, 10)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    Z = con(universe_new)
    ax.set_zlim(0, 12)
    ax.plot_surface(_xx, _yy, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.view_init(60, 35)

    return ax


fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection="3d")
anim = animation.FuncAnimation(fig=fig, func=updata(universe), frames=np.arange(0, 30), init_func=None, interval=100)

anim.save('风化模型.gif', writer='pillow')
plt.show()
