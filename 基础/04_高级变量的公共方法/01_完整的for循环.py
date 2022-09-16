"""
完整的for循环语句结构：
for 变量 in 集合:
    循环体代码

else:
    循环结束后，会执行的代码
"""
for i in range(3):
    print(i)
else:
    print("i循环结束")


# 如果有循环体内部通过了break，则else也不会运行
for a in range(3):
    print(a)
    if a == 2:
        break
else:
    print("a循环结束")