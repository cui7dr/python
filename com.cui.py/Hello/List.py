"""
列表的基本使用及相关操作
"""

# 定义一个列表
name_list = ["zhangsan", "lisi", "wangwu"]

# 索引取值
print(name_list[2])  # list index out of range --列表索引超出范围
# 根据数据内容确定数据位置
print(name_list.index("lisi"))

# 修改数据
name_list[0] = "张三"  # list assignment index out of range --列表指定的索引超出范围，程序会报错！
print(name_list)

# 增加数据
# append 方法可以向列表末尾追加数据
name_list.append("zhaoliu")
print(name_list)
# insert 方法可以在列表指定索引位置插入数据
name_list.insert(1, "王小二")
print(name_list)
# extend 方法可以把其他列表中完整数据追加到当前列表末尾
temp_list = ["孙悟空", "猪悟能", "沙悟净"]
name_list.extend(temp_list)
print(name_list)

# 删除数据
# remove 可以从列表中删除指定数据
name_list.remove("wangwu")
print(name_list)
# pop 方法默认删除列表最后一个元素
name_list.pop()
print(name_list)
# pop 方法指定删除元素的索引
name_list.pop(2)
print(name_list)

# 使用 del(delete) 关键字删除列表元素
del name_list[2]
print(name_list)

# len(length) 函数可以统计列表中元素总数
list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len)

# count 可以统计列表中某一元素出现的次数
name_list.append("张三")
count = name_list.count("张三")
print("张三出现了 %d 次" % count)

# 从列表中删除第一次出现的数据，如果数据不存在，程序会报错
name_list.remove("张三")
print(name_list)

# 列表排序
num_list = [6, 8, 4, 1, 10]

# 升序
name_list.sort()
num_list.sort()
print(name_list)
print(num_list)

# 降序
name_list.sort(reverse=True)
num_list.sort(reverse=True)
print(name_list)
print(num_list)

# 逆序（反转
name_list.reverse()
num_list.reverse()
print(name_list)
print(num_list)

# 使用迭代遍历列表  --顺序的从列表中依次获取数据并放到新的变量，在循环体内部可以访问到当前这一次获取到的数据
for name in name_list:
    print("名字是 %s" % name)

# clear 清空列表
name_list.clear()
print(name_list)

# del 是将变量从内存中删除，删除列表元素，建议使用列表提供的方法
name1 = "小明"
del name1
print(name1)
