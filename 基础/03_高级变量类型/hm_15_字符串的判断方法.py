# 1. string.isspace：如果string只包含空格，则返回True
# 转义字符串中\t制表符，\n换行，\r回车 都识别成空格
str = "        \t\n\r"
print(str.isspace())

# 2. string.isdecimal：如果string只包含数字，则返回True
# 全角数字
str = "1"
print(str.isdecimal())

# 3. string.isdigit：如果string只包含数字，则返回True
# 全角数字，（1），\u00b2
str = "\u00b2"
print(str.isdigit())

# 4. string.isnumeric：如果string只包含数字，则返回True
# 全角数字，汉字数字
str = "一百"
print(str.isnumeric())
