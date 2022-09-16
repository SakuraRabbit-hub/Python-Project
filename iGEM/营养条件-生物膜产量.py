import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.rc('font', family='SimHei', size=7)

# 读取数据
data = pd.read_excel(io=r"C:\Users\xingz\Desktop\igem\建模组\8.19\营养条件-生物膜产量.xlsx")
data.head()

# 拟合函数
x = data['葡萄糖浓度/（mmoL/L）']
y = data['A650/A600']
f = np.polyfit(x, y, 2)
print(f)
print(np.poly1d(np.polyfit(x, y, 1)))
fity = f[0] * x + f[1]

# 画图
plot1 = plt.plot(data['葡萄糖浓度/（mmoL/L）'], data['A650/A600'], 'b', label = 'original values')
plot2 = plt.plot(x, fity, 'r')

plt.xlabel('葡萄糖浓度/（mmoL/L）')
plt.ylabel('A650/A600')
plt.grid(True, linestyle = '--', alpha = 0.5)
plt.legend()
plt.title('origin values')
plt.show()