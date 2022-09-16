# elif必须在if-else使用，有多少个条件就可以写多少个elif
# 应用场景是：同时 判断 多个条件，所有条件都是平级的

"""
if-elif-else基本语法：
if 条件1:
elif 条件2:
elif 条件3:
……
else:
"""
holiday_name = "妇女节"
print(holiday_name)

if holiday_name == "情人节":
    print("买玫瑰")
elif holiday_name == "平安夜":
    print("吃大餐")
elif holiday_name == "生日":
    print("买蛋糕")
else:
    print("每天都是节日啊")
