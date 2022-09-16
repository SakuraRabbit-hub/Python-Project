info_tuple = ("xiaoming", 18, 1.75)

# 1. 使用迭代遍历元组
for my_info in info_tuple:
    # 用格式化字符串拼接 my_info 这个变量是不方便的
    # 因为元组中通常保存的数据类型不同
    print(my_info)


# 2. 格式化字符串后面的（）本质上就是元组
print("%s 的年龄是 %d, 身高是 %.2f" % info_tuple)
# 同样可以使用格式化字符串来拼接成一个新的字符串
info_str = "%s 的年龄是 %d, 身高是 %.2f" % info_tuple
print(info_str)


