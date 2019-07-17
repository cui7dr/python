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

# 判断字符串是否以指定字符串开始
print(str1.startswith("hello"))
# 判断字符串是否以指定字符串结束
print(str1.endswith("python"))
# 查找指定字符串在字符串中位置
print(str1.find("llo"))
# 如果 find() 指定的字符串不存在，返回 -1 （index 会报错
print(str1.find("aaa"))
# 替换字符串（不会修改原有字符串内容，会返回一个新的字符串
print(str1.replace("python", "world"))
print(str1)

# 字符串文本对齐
poem = ["\t\n登鹳雀楼", "王之涣", "白日依山尽\t\n", "黄河入海流", "欲穷千里目", "更上一层楼"]
for poem_str in poem:
    # 先使用 strip() 去除字符串中的空白字符，再使用 center() 文本居中
    print("|%s|" % poem_str.strip().center(10, " "))

poem1 = "登鹳雀楼\t王之涣\t白日依山尽\t\n黄河入海流\t\t欲穷千里目\t\t\n更上一层楼"
print(poem1)
# 拆分字符串
poem_list = poem1.split()
print(poem_list)
# 合并字符串
result = " ".join(poem_list)
print(result)
