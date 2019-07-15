"""
  字符串的定义和基本使用
"""

str1 = "hello python"
str2 = '我的外号是"大黄瓜"'

print(str1)
print(str2)

# 字符串的遍历
for char in str2:
    print(char)

# 字符串长度
print(len(str1))

# 某个字符串出现的次数
print(str1.count("o"))
print(str1.count("123"))

# 某个字符串出现的位置
print(str1.index("py"))
# 如果使用 index 传递的字符串不存在会报错
#print(str1.index("aaa"))
