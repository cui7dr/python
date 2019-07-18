"""
  for 语法及遍历
"""

for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
    # 如果循环体内部使用 break 退出循环， else 不会被执行
    else:
        print("不会执行")
print("over")

# 遍历字典列表
students = [{"name": "张三"}, {"name": "李四"}]
print(students)

# 在学生列表搜索指定的名字
find_name = "王五"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        break
    else:
        print("没有找到 %s" % find_name)
print("over")
