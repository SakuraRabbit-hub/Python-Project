num_list = [4, 5, 3, 10, 30, 24]
name_list = ["yi", "san", "jiu", "10"]
# 1. 升序
# 对数字：从小到大排序
num_list.sort()
print(num_list)
# 对字符：按字母顺序排序
name_list.sort()
print(name_list)

# 2. 降序
num_list.sort(reverse=True)
print(num_list)
name_list.sort(reverse=True)
print(name_list)


# 3. 逆序（反转）
num_list.reverse()
print(num_list)