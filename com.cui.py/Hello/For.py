"""
  for 语法
"""

for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
    # 如果循环体内部使用 break 退出循环， else 不会被执行
    else:
        print("不会执行")
print("over")
