# 实际开发中对字典的循环遍历需求并不多
"""
# 格式
for 循环内部使用的“key的变量” in 字典:
"""
xiaoming_dict = {"name": "xiaoming",
                 "qq": "123456",
                 "phone": "10086"}

# 迭代遍历字典
# 变量k是每一次循环中，获取到的键值对的key
for k in xiaoming_dict:
    print("%s - %s" % (k, xiaoming_dict[k]))
