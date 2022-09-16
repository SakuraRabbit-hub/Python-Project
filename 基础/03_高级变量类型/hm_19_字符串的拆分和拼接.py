poem_str = "登鹳雀楼#王之涣\t 白日#依山尽\t \n黄河入#海流\t\t欲穷#千里目\n上一层楼"

print(poem_str)

"""
1. 拆分字符串
string.split(str="", num)
以str为分隔符拆分string，如果num有指定值，则仅分隔 num+1 个子字符串
str默认包含 \r, \t, \n和空格
"""
poem_list = poem_str.split()
print(poem_list)

poem_jin = poem_str.split("#", 3)
print(poem_jin)


"""
2. 合并字符串
string.join(seq)
以string作为分隔符，将seq中所有的元素（的字符串表示）合并成一个新的字符串
"""
result = " ".join(poem_list)
print(result)

result2 = "!".join(poem_list)
print(result2)