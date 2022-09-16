import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import constants
from sympy import *

# 读取数据
data = pd.read_excel(io=r"C:\Users\xingz\Desktop\iGEM\建模组\野生荧光假单胞菌生长曲线数据.xlsx")


def func(t, a, b, c):
    return 0.012*pow(10,a*np.exp(-np.exp(b-c*t)))


popt, pcov = curve_fit(func, data['time'], data['data'])
print(popt)

# 原始曲线
plot1 = plt.plot(data['time'], data['data'], 'b', label = 'original values')

# 拟合出的曲线
plot2 = plt.plot(data['time'], func(data['time'],popt[0],popt[1],popt[2]), 'r', label = 'curve fit values')
plt.grid(True, linestyle = '--', alpha = 0.5)
plt.xlabel('time')
plt.ylabel('data')
plt.legend()
plt.title('COMPARISON')
plt.show

umax = popt[0] * popt[2] / constants.e
n, t, u = symbols('n t u')
n = 0.012 * 10 ** (popt[0] * exp(-exp(popt[1]-popt[2]*t)))

u = diff(n, t) / n
print(u)
print(u / umax)
