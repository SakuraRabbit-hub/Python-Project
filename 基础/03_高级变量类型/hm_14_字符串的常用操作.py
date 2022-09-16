hello_str = "hello hello"

# 1. 统计字符串长度
print(len(hello_str))

# 2. 统计某一个子字符串出现的次数，若不存在则返回0
print(hello_str.count("llo"))
print(hello_str.count("abc"))

# 3. 某一个子字符串出现的第一个位置
print(hello_str.index("llo"))
# 注意：子字符串不存在时就会报错
# print(hello_str.index("abc"))

# 4. 从子符串中取出单个字符
print(hello_str[6])

# 5， 字符串的第一个字符大写
print(hello_str.capitalize())

# 6， 字符串的每个单词的第一个字符大写
print(hello_str.title())

# 7， 字符串的所有字符大写
print(hello_str.upper())

# 8， 字符串的所有字符小写
print(hello_str.lower())

# 9. 反转str中的大小写
print(hello_str.swapcase())