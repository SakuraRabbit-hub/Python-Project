# open默认以 只读 的方式发开文件
# 语法： f = open('文件名', '访问方式')

"""
r: 只读，指针在文件开头
w: 只写，如果文件存在就覆盖，不存在就创建新文件
x: 创建写模式
a: 追加，指针在文件结尾
r+: 读写，指针在开头
w+: 读写
a+: 读写，指针在末尾
"""

# 1. 打开
file = open('readme', 'a+')

# 2. 写入文件
file.write('123')

# 3. 关闭
file.close()

file = open('readme', 'r')
text = file.read()
print(text)
