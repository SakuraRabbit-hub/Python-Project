# 分支语句：根据条件判断，决定执行代码的分支

# 必须记住规定输入字符的类型！input默认返回str类型
# 不同类型之间不能直接比较
age = int(input("请输入年龄："))

if age >= 18:
    print("请进！")
else:
    print("抱歉！")


"""
print(value1, value2, ..., sep = '', end = ' \n', file = sys.stdout, flush = False)
sep: 用于指定输出数据之间的分隔符，默认为空格
end: 换行还是不换行，默认换行，当为空格时不换行
file: 用于指定输出位置，默认为控制台，当为文件名时定向输出到文件
flush: 将缓存中的内容立即输出到控制台，实时显示
"""


