"""
循环语法
"""

# 定义一个整数变量，记录循环次数
i = 0
# 开始循环
while i < 5:
    # 循环体
    print("Hello Python While")
    # 处理计数器
    i += 1  # i = i + 1
# 查看循环后计数器的值
print("循环后 i = %d" % i)
print("------------")

"""
计算 0-10 累加和
"""
# 定义一个最终结果的变量
total1 = 0
i1 = 0
# 开始循环
while i1 <= 10:
    print(i1)
    # 每次循环记录 total
    total1 += i1
    # 处理计数器
    i1 += 1
# 最终结果
print("0-10 求和结果 = %d" % total1)
print("------------")

"""
计算 0-10 偶数累加和
"""
# 定义一个最终结果的变量
total2 = 0
i2 = 0
# 开始循环
while i2 <= 10:
    # 判断偶数
    if i2 % 2 == 0:  # 奇数 i % 2 != 0
        print(i2)
        # 当 i 为偶数进行累加
        total2 += i2
    # 处理计数器
    i2 += 1
# 最终结果
print("0-10 偶数求和结果 = %d" % total2)
print("------------")

"""
break 满足某一条件时，退出循环
"""
i3 = 0
while i3 < 10:
    if i3 == 3:
        break
    print(i3)
    i3 += 1
print("循环结束")
print("------------")

"""
continue 满足某一条件时，不执行后续重复代码
注意：在循环中，如果使用 continue 这个关键字，在使用关键字之前，需要确认循环的计数是否修改，否则可能会导致死循环
"""
i4 = 0
while i4 < 10:
    if i4 == 3:
        i4 += 1
        continue
    print(i4)
    i4 += 1
print("------------")

"""
打印 * ，每行依次递增
"""
i5 = 1
while i5 <= 5:
    print("*" * i5)
    i5 += 1
print("------------")

"""
嵌套循环打印 * ，每行数量和行数一致
"""
i6 = 1
while i6 <= 5:
    # 定义一个整数变量，记录每列 * 显示
    j6 = 1
    while j6 <= i6:
        print("*", end="")  # print("%d", %j6)
        j6 += 1
    print("")  # 增加换行
    i6 += 1
print("------------")

"""
九九乘法表
"""
i7 = 1
while i7 <= 9:
    j7 = 1
    while j7 <= i7:
        print("%d * %d = %d" % (j7, i7, j7 * i7), end="\t")
        j7 += 1
    print("")
    i7 += 1
print("------------")

"""
转义字符
"""
# \t 制表符，协助输出文本 垂直方向 对齐
print("1\t2\t3")
print("10\t20\t30")
print("------------")
# \n 换行符
print("Hello\nPython")
print("------------")
# \" 输出"
print("Hello\"World\"")
print("------------")
