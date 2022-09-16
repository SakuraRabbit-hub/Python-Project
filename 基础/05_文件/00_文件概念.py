"""
文本文件：
①可以使用文本编辑软件查看
②本质还是二进制文件

二进制文件：
①图片文件、音频文件等
②需要专门的软件打开，不能让人直接阅读
"""

# 1. 打开文件：open("文件名")
file = open('readme')

# 2. 读、写文件: read\write
text = file.read()
print(text)

# 3. 关闭文件: close
file.close()