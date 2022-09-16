students = [{'name': 'xiaoming'},
            {'name': 'xiaomei'}]

print("第一次测试")
for stu_dict in students:
    print(stu_dict)

print("循环结束")
print('------')

# 在学员列表中搜索指定的姓名
print("第二次测试")
find_name = 'xiaoming'
for stu_dict in students:
    if stu_dict['name'] == find_name:
        print("已经找到{}".format(find_name))
        # 已经找到，就不再继续往下找
        break

else:
    print("没有找到")
print('------')
