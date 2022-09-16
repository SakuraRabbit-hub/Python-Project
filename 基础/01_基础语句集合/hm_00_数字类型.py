"""
1. int(): 整数类型
2. float(): 浮点数类型
3. complex(): 复数类型
"""

# abs: 计算实数的绝对值或者复数的模
print(abs(-3))
print(abs(-3 + 4j))

# divmond: 同时计算两个数字的整数商和余数
print(divmod(8, 5))

# pow: 幂运算, pow(a, b, c)表示a、b幂运算后再除以c取余数
print(pow(2, 3))
print(pow(2, 3, 5))

# round(a/b, c): 四舍五入，保留c位小数
print(round(8/3, 2))