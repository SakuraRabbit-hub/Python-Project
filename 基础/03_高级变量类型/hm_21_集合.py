# 集合：元素之间无序、唯一
# 集合 = {元素1, 元素2, ...}

set1 = {3, 5, 9}
print(set1)

# 创建一个空集合
set2 = set()
print(type(set2))

# 将元组、列表等转换成集合时，会先进行去重
list = [1, 1, 2, 4, 5, 5, 5, 8]
print(set(list))

# 将字典转换为集合时，呈现的是键
dic = {'name': 'xiaoming',
       'age': 18,
       'height': 1.75}
print(set(dic))