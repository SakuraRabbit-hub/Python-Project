"""
文件指针：标记从哪个位置开始读取数据
第一次打开文件时指向文件的开始位置
执行read以后指向读取内容的末尾（默认为文件末尾）
"""

# 1. 打开文件：open("文件名")
file = open('readme')

# 2. 读、写文件: read\write
text = file.read()
print(text)
print('-' * 30)

text = file.read()  # 再调用时就读取不到任何内容了，因为执行上一个read以后文件指针在内容末尾
print(text)
print('*' * 20)
# 3. 关闭文件: close
file.close()

# 文件.read(n)表示读n个字符，指针也会移动
# 获取文件指针的值：文件名赋值.tell()
# 移动指针：文件名.seek(偏移量，定位)