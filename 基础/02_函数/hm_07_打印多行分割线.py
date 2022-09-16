# 任务：在06的基础上，实现打印任意行分割线
# 提示：不要一有变化就疯狂改变原来写好的函数，可以考虑嵌套


def pri_line(char, times):
    """打印单行分隔线 """
    print(char * times)


def pri_lines(char, times):
    """打印多行分隔线
    :param char: 所打印的字符
    :param times: 单行的打印次数
    """
    row = 0
    lines = int(input("请输入行数："))
    while row < lines:
        pri_line(char, times)
        row += 1


pri_lines("*", 5)
