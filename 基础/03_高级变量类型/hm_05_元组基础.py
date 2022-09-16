"""
元组： 由多个元素组成的序列，用（）定义，索引从0开始
元组和列表的区别：元组内的任何元素都不能修改
很少使用空元组
"""


info_tuple = ("xiaoming", 18, 1.75)
print(type(info_tuple))

# 想要定义一个只包含一个元素的元组，需要在元素后加，
single_int = (5)
print(type(single_int))
single_tuple = (5,)
print(type(single_tuple))

# 元组能使用的方法
# 1. 取值和取索引
print(info_tuple[0])
print(info_tuple.index("xiaoming"))

# 2. 统计某元素出现的次数
print(info_tuple.count("xiaoming"))

# 3. 统计元组长度
print(len(info_tuple))