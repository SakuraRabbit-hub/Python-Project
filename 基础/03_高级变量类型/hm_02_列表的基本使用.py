list = ["yi", "er", "san"]

# 1. 取值和取索引
# list index out of range - 列表索引超出范围
print("①", list[2])
# 知道数据的内容，想确定数据在列表中的位置
print("②", list.index("er"))

# 2. 修改
list[1] = "si"
print("③", list)

# 3. 增加
# 向末尾追加数据
list.append("wu")
print("④", list)

# 向指定索引位置插入数据
list.insert(1, "liu")
print("⑤", list)

# 插入列表
list_extend = ["zengjia", "yige", "liebiao"]
list.extend(list_extend)
print("⑥", list)

# 4. 删除
# del: 删除指定索引数据(默认删除最后一个)
    # 本质上是将一个变量从内存中删除，后续代码中就无法再使用这个变量了
del list[6]
print(list)

# pop: 删除指定索引数据(默认删除最后一个)
list.pop()
print("⑦", list)
list.pop(3)
print("⑧", list)

# 删除列表中某个值的第一个匹配项
list.insert(5, "yi")
print("⑨", list)
list.remove("yi")
print("⑩", list)

# 清空列表
list_extend.clear()
print(list_extend)

# 5. 统计
list.append("ba")
print(list)
listzengjia = ["yi", "er", "ba"]
list.extend(listzengjia)
list.extend(list)
print(list)

# len: 统计列表元素总数
print(len(list))

# count: 统计指定元素出现的次数
print(list.count("yi"))
