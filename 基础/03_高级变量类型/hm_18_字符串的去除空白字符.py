poem = ["   登鹳雀楼",
        "王之涣   ",
        "白日  依山尽",
        "黄河入海流  ",
        "  欲穷千里目",
        "更上一层楼  "]

for poem_str in poem:
        print("|%s|" % poem_str)
"""
1. string.lstrip()：截掉string左边（开始）的空白字符
"""
for poem_str in poem:
        print("|%s|" % poem_str.lstrip())

"""
2. string.rstrip()：截掉string右边（结尾）的空白字符
"""
for poem_str in poem:
        print("|%s|" % poem_str.rstrip())

"""
3. string.strip()：截掉string左右两边的空白字符
"""
for poem_str in poem:
        print("|%s|" % poem_str.strip())