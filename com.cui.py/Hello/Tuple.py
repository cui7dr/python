"""
 元组的基本使用和遍历/格式化字符串
"""

info_tuple = ("张三", 20, 1.81, "张三")
# 根据索引取值
print(info_tuple[0])
# 已知数据内容，获取对应的索引
print(info_tuple.index("张三"))
# 统计计数
print(info_tuple.count("张三"))
# 获取元组中包含元素的个数
print(len(info_tuple))

# 使用迭代遍历元组
for zs_info in info_tuple:  # 使用格式字符串拼接 zs_info 这个变量不方便！因为元组中通常保存的数据类型是不同的！
    print(zs_info)

# 格式化字符串
print("%s 年龄是 %d 身高是 %.2f ,%s" % info_tuple)
# 格式化后面的本质上就是元组
info_str = "%s 年龄是 %d 身高是 %.2f ,%s" % info_tuple
print(info_str)
