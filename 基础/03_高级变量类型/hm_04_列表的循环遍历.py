"""
遍历：从头到尾 依次从列表中获取数据
    在循环体内部 针对每一个元素，执行相同操作
    使用 for 来实现迭代遍历
格式：
for 循环内部使用的变量 in 列表:
    循环内部针对列表元素进行操作
每一次循环过程，数据都会保存在这个变量中
"""


name_list = ["yi", "er", "san"]
for my_name in name_list:
    print("我的名字叫 %s" % my_name)