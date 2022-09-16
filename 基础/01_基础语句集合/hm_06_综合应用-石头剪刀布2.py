"""
需求：
①从控制台输入：石头（1）/剪刀（2）/布（3）
②电脑随机出
③比较胜负
增加用到的知识点：
随机数
"""

# 导入random包，调用random.randint(a,b)
# 返回[a,b]间的任意整数
import random
computer = random.randint(1, 3)

player = int(input("请输入您要出的："))
print("玩家出的是 %d , 电脑出的是 %d" % (player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家胜")

elif player == computer:
    print("平局")

else:
    print("电脑胜")
