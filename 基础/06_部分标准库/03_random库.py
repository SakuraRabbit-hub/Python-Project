# 需求：随机输出一个收集品牌屏幕输出
import random

"""
1. seed(a = None): 初始化随机数种子，默认为当前系统的时间
2. random(): 生成一个[0.0, 1.0]之间的随机小数
3. randint(a, b): 生成一个[a, b]之间的整数
4. sample(pop, k): 从pop类型中随机选取k各元素，以列表类型返回
"""
brandlist = ['oppo', 'vivo', '1', '2', '3']
random.seed(2)  # 如果设置了随机数种子，那之后再运行都是固定的值
name = random.sample(brandlist, 2)
print(name)

