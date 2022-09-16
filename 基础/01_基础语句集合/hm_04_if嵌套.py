# if嵌套应用场景：希望在条件成立的执行语句中，再增加条件判断
# 嵌套的if也要比上一层if多一个缩进

"""
定义布尔类型变量 has_ticket 表示是否有车票
定义整型变量 knife_length 表示刀的长度，单位为厘米
先检查车票：有才能过安检，没有则不能上车
再检查刀：长度超过20不能上车
"""
has_ticket = False
knife_length = True
# 不要尝试让input内容输出为布尔类型，无论输入啥都会是True
# 可以input("True or False?")，然后比较 if XX == "True":
if has_ticket:
    print("可以过安检")
    if knife_length:
        knife_length = int(input("请输入刀长："))
        if knife_length >= 0 and knife_length <= 20:
            print("安检通过，请上车。")
        else:
            print("安检未通过，不允许上车。")
else:
    print("无车票，不允许上车。")
