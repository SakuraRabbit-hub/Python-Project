# 1. 打开文件
file_read = open('readme')
file_dup = open('dupbig', 'w')

# 2. 读、写
while True:
    text = file_read.readline()

    if not text:
        break

    file_dup.write(text)

# 3. 关闭
file_read.close()
file_dup.close()
