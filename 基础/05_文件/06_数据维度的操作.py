f = open('123.csv', 'w+')

f.writelines(['姓名, 语文, 数学, 合计'])

f.seek(0)

print(f.read())

list = [['张三, 93, 94, 95'], ['李四, 78, 79, 77']]
for i in list:
    f.write(','.join(i) + '\n')

f.seek(0)

print(f.read())
