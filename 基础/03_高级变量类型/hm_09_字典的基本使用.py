xiaoming_dic = {"name": "小明"}

# 1. 取值
print("①", xiaoming_dic["name"])

# 2. 增加/修改
# 如果key不存在，就新增键值对
xiaoming_dic["age"] = 18
print("②", xiaoming_dic)
# 如果key存在，就修改键值对
xiaoming_dic["name"] = "小白"
print("③", xiaoming_dic)

# 3. 删除
xiaoming_dic.pop("name")
print("④", xiaoming_dic)