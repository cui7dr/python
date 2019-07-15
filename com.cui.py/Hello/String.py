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
# print(str1.index("aaa"))

# 判断空白字符串
space_str = "    \t\n\r"
print(space_str.isspace())

# 判断字符串是否小数（结果都为 false
num_str = "1.2"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
# unicode 字符串（T/F/F
unicode_str = "\u00b2"
print(unicode_str)
print(unicode_str.isdecimal())
print(unicode_str.isdigit())
print(unicode_str.isnumeric())
# 判断中文数字（F/F/T
textNum_str = "一千零一"
print(textNum_str)
print(textNum_str.isdecimal())
print(textNum_str.isdigit())
print(textNum_str.isnumeric())
