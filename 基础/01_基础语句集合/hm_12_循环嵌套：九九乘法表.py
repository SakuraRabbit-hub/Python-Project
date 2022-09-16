row = 1
while row <= 9:

    col = 1
    while col <= row:
        # \t表示在垂直方向上对齐
        print("%d * %d = %d" % (col, row, col*row), end=" \t")
        col += 1

    print("")
    row += 1
