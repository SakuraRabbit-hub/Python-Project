hello_str = "hello, world"


"""
1. string.startswith(str)：
检查字符串是否是以 str 开头，是则返回True
"""
print(hello_str.startswith("e"))


"""
2. string.endswith(str):
检查字符串是否是以 str 结尾，是则返回True
"""
print(hello_str.endswith("world"))


"""
3. string.find(str, start, end)：检测str是否包含在string中
如果在start和end指定范围，则检查是否在指定范围内，是则返回开始的索引值，否则返回-1
"""
print(hello_str.find("llo"))
print(hello_str.find("abc"))
print(hello_str.find("llo", 0, 6))


"""
4. string.replace(old_str, new_str, num = string.count(old):
把string中的old_str替换成new_str，如果num指定，则替换不超过num次
"""
print(hello_str.replace("hel", "python"))
hello_str.replace("hel", "python")
print(hello_str)
# ！！！replace在执行以后只能返回一个新的字符串，但不会修改原有字符串的内容
# 只能用一个新变量接收新的字符串
python_str = hello_str.replace("world", "python")
print(python_str)