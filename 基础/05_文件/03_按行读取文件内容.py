"""
f.readline(size): 一次读取一行，每次读取完就把指针移到下一行。指定size时读入该行size个字符
f.readlines(hint): 从文件中读入hint行
"""
file = open('readme')

while True:
    text = file.readline()
    # 判断是否读取到内容
    if not text:
        break
    print(text)

file.close()
