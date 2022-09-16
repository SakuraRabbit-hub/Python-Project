num_list = [1, 2, 3]
name_tuple = ("yi", "er", "san")

# 用list把元组转化成列表，要设置新变量接收列表信息
name_list = list(name_tuple)
print(type(name_list))
print(name_list)

# 用tuple把列表转化成元组，要设置新变量接收元组信息
num_tuple = tuple(num_list)
print(type(num_tuple))
print(num_tuple)
