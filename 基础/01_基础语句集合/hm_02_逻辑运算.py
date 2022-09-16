# 逻辑运算符包括与and/或or/非not

# and练习：年龄在0~120间达标
age = 90
if age >= 0 and age <= 120:
    print("年龄达标")
else:
    print("年龄不达标")

# or练习：两门成绩有一门及格则成绩合格
python_score = 80
c_score = 40
if python_score >= 60 or c_score >= 60:
    print("成绩合格")
else:
    print("成绩不合格")

# not练习：非本公司员工不能进入（定义一个布尔变量）
# 在开发中，通常希望某个条件不满足时，执行一些代码，可以用not
# 另外，如果需要拼接复杂的逻辑计算条件，同样也有可能使用到not
is_employee = True
if not is_employee:
    print("非本公司人员，请勿入内")
