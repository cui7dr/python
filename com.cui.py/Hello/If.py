"""
If 语法
"""
# 导入随机工具包，放在文件顶部 import random
import random

# 定义整数变量
num = 10
num1 = 20

# 判断大小
if num >= 12:
    print("大于")
else:
    print("小于")
print("无论大小始终执行")

# 判断数字是否介于某两个值中间
if 0 <= num <= 100:  # 与/或：and/or
    print("是")
else:
    print("否")

# 判断任一数大于 15
if num > 15 or num1 > 15:
    print("至少有一个数大于 15")
else:
    print("都不大于 15")

# 定义布尔类型
man = True
# 判断男女
if not man:
    print("女")
"""
  在开发中，通常希望某个条件不满足时，执行一些代码，可以使用 not
  另外，如果需要拼接复杂的逻辑计算条件，同样也有可能使用到 not
"""

# 定义字符串
day = "元旦节"
# 判断节日
if day == "劳动节":
    print("五一放假")
elif day == "国庆节":
    print("十一放假")
elif day == "元旦节":
    print("元旦放假")
else:
    print("工作")

# 多层判断
if man:
    print("性别男")
    if num < 18:
        print("未成年，%d 岁" % num)
    else:
        print("成年")
else:
    print("女生")

# 剪包锤游戏
# 玩家从控制台输入----1.石头/2.剪刀/3.布
player = int(input("请输入----1.石头/2.剪刀/3.布："))
# 机器随机
computer = random.randint(1, 3)
print("玩家选择是 %d vs 电脑是 %d" % (player, computer))
# 比较胜负
if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("赢了")
elif player == computer:
    print("平局")
else:
    print("输了")
