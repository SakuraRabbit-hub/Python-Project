"""
需求：
①从控制台输入：石头（1）/剪刀（2）/布（3）
②电脑固定出
③比较胜负
用到的知识点：
①格式化字符串 %d
②逻辑运算符
③if-elif-else
④if条件加大括号，内部可以换行，减少阅读困难
"""
player = int(input("请输入您要出的："))
computer = 2
print("玩家出的是 %d , 电脑出的是 %d" % (player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家胜")

elif player == computer:
    print("平局")

else:
    print("电脑胜")
