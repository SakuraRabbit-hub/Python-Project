"""
continue: 只在循环语句使用，且只针对当前循环
某一条件满足时，不执行后续重复的代码，返回到while那一行
"""
# 注意：如果使用continue，必须确认循环的计数是否修改，否则可能会死循环
i = 0
while i < 10:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
print("over")
