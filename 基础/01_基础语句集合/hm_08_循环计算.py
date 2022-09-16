# 计算0~100之间所有数字的累加结果
n = 0
i = 0
while i <= 100:
    n += i
    i += 1
print("n = %d" % n)

# 计算0~100之间所有奇数之间的累加结果
result = 0
i = 0
while i <= 100:
    if i % 2 != 0:
        print(i)
        result += i
    i += 1
print("result = %d" % result)
