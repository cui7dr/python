def test1():
    print("*" * 10)


def test2():
    print("-" * 10)
    # 函数嵌套调用
    test1()
    print("+" * 10)


test2()


# 打印分割线
def print_line(char, time):  # param char：分割字符    param time：重复次数
    print(char * time)


print("p" * 10)


# 打印多行分割线
def print_lines(chars, times):
    row = 0
    while row < 5:
        print_line(chars, times)
        row += 1


name = "python"
print_lines("y", 10)
