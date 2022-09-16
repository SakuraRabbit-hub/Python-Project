poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:
    print(poem_str)
"""
1. string.ljust(width)
返回一个原字符串左对齐，并使用空格填充至长度width的新字符串
"""
for poem_str in poem:
    print("|%s|" % poem_str.ljust(10," "))

"""
2. string.rjust(width)
返回一个原字符串右对齐，并使用空格填充至长度width的新字符串
"""
for poem_str in poem:
    print("|%s|" % poem_str.rjust(10," "))

"""
3. string.center(width, fillchar)
返回一个原字符串居中对齐，并使用fillchar(默认空格)填充至长度width的新字符串
"""
for poem_str in poem:
    print("|%s|" % poem_str.center(10,"="))
## 等价于格式化字符串 print("{:=^10}".format(poem_str))
for poem_str in poem:
    print("|{:=^10}|".format(poem_str))