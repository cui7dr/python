"""
  字典的定义和基本使用
"""

# 字典是无需的数据集合，使用 print 函数输出的时候，通常输出的顺序和定义的顺序是不一致的
zhangsan = {"name": "张三",
            "age": 21,
            "height": 180,
            "weight": 75}
print(zhangsan)

# 在字典中取值
print(zhangsan["name"])
# 取值的时候，如果指定的 Key 不存在，会报错
# print(zhangsan["name1"])

# 如果 Key 不存在，会增加新的键值对
zhangsan["sex"] = "男"
print(zhangsan)
# 如果 Key 已存在，会修改已经存在的值
zhangsan["age"] = 23
print(zhangsan)

# 删除（如果 Key 不存在，会报错
zhangsan.pop("sex")
print(zhangsan)

# 统计键值对数量
print(len(zhangsan))

# 定义新的字典
vhsj = {"sex": "男",
        "age": 25}
print(vhsj)
# 合并字典（如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值
zhangsan.update(vhsj)
print(zhangsan)

# 清空字典
vhsj.clear()
print(vhsj)

# 迭代遍历字典
for k in zhangsan:  # 变量 k 是每次循环中获取到键值对的 Key
    print("%s - %s" % (k, zhangsan[k]))

# 将多个字典存在一个列表中
info_list = [{"name": "张三", "tel": 123}, {"name": "李四", "tel": 321}]
# 遍历列表
for info_one in info_list:
    print(info_one)
