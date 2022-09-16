"""
break: 专门在循环中使用，只针对当前所在的循环有效。
某一条件满足时，退出循环，不再执行后续重复的代码
"""
i = 0

while i < 10:
    if i == 3:
        break
    print(i)
    i += 1
print("over")
