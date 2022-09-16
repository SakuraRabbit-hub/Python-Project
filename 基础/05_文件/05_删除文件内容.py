# f.truncate(size): size为字节数，从头计算的第size个字节数位置，删除后面所有内容

file = open('readme', 'r+')

file.truncate(7)

file.close()