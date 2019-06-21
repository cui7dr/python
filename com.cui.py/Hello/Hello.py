"""
python 变量定义及简单运算
"""

print("Hello World !")
print("Hello Python")

# 注释
print("单行注释")
"""
 多行注释
"""
print("多行注释")
print("行注释")  # 注释

# 定义一个变量
num = "123456"
# 在控制台输出变量内容
print(num)

"""
 简单运算
"""
num1 = 8
num2 = 4
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2
print(add)
print(subtract)
print(multiply)
print(divide)

"""
 数据类型
 在运行的时候，解释器会根据赋值语句等号右侧的数据，自动推导出变量中保存数据的准确类型
"""
# str 表示字符串类型
name = "小明"
# int 表示整数类型
age = 18
# bool 表示布尔类型 ( True/False
gender = True
# float 表示浮点类型
height = 1.8

# 在控制台输入值
age1 = input("输入年龄：")
"""
 类型转换
 将输入值转成 int
 字符串不能参与运算
"""
ageInt = int(age1)
# 进行运算
total = ageInt + add
# 输出结果
print(total)

# 控制台输入 int 值
age2 = int(input("输入年龄："))
print(age2)

# 定义字符串变量 name
name1 = "小明"
print("我的名字叫 %s，请多多关照！" % name1)

# 定义整数变量 student_no，输出 我的学号
student_no = 100123456
print("我的学号是 %06d" % student_no)

# 定义小数 price、weight、money，
# 输出 单价 8.50 元／斤，购买了 7.50 斤，需要支付 金额
price = 8.5
weight = 7.5
money = price * weight
print("单价 %.1f 元／斤，购买了 %.2f 斤，需要支付 %.2f 元" % (price, weight, money))

# 定义一个小数 scale，输出 数据比例是 10.00%
scale = 0.8
print("数据比例是 %.2f%%" % (scale * 100))
