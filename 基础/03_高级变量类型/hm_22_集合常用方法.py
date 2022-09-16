set1 = {1, 3, 5, 7, 9}
set2 = {2, 4, 3, 5, 8}
print(set1, set2)
'''
1. 增加：
集合.add(新元素)：若存在，则不加
集合.update(新集合)：忽略重复元素
'''
set1.add(8)
set2.update(set1)
print(set1, set2)

'''
2. 删除：
set.discard(): 删除一个指定元素，元素不存在则不执行
set.remove(): 删除一个指定元素，元素不存在则提示异常
set.pop(): 随即删除并返回集合中被删除的元素
set.clear(): 清空集合
del set: 删除整个集合
'''
set2.discard(9)
print(set2)

print(set1.pop())
print(set1)

'''
3. 查询
len(集合)
in/not in
'''
print(1 in set1)


'''
4. 其他运算
内置函数max(), min(), sum(),...
数学意义上的：
①交集：set1 & set2
②并集：set1 | set2
③差集：set1 - set2
④对称差集：set1 ^ set2
⑤包含关系：set1 < set2
'''