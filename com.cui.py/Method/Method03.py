# 带参函数
def Method03(num1, num2):
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))
    # 使用返回值表示函数执行结果
    return result


Method03(11, 2)
# 定义一个变量接收函数结果
method03_result = Method03(10, 12)
print("计算结果：%d" % method03_result)
