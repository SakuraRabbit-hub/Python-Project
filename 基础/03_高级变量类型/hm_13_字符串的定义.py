"""
1. 字符串 就是 一串字符，是编程语言中表示文本的数据类型
2. 定义：通常是" "
3. 索引：获取一个字符串中指定位置的字符，仍然从0开始
4. for 迭代遍历
"""

# 字符串的定义
str1 = "hello, python"
str2 = "lalala'dada'"
print(str1)
print(str2)

# 索引
print(str1[6])

# 遍历
for char in str2:
    print(char, end="")