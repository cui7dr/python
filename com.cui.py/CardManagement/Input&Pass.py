"""
  名片管理
"""

# 02 ---- 添加无限循环，由用户决定退出
while True:

    # 04 ---- 添加 TODO 注释
    # TODO (张三) 显示功能菜单

    # 01 ---- start
    action_str = input("请输入你希望执行的操作：")
    print("你选择的操作是【%s】" % action_str)

    # 1，2，3 操作选项
    if action_str in ["1", "2", "3"]:
        # pass
        # 03 ---- start 添加嵌套操作
        if action_str == "1":
            pass
        elif action_str == "2":
            pass
        elif action_str == "3":
            pass
        # 03 ---- end
    # 0 退出
    elif action_str == "0":
        print("欢迎再次使用")
        break
        # pass
    # 如果在开发程序时，不希望立刻编写分支内部的代码
    # 可以使用 pass 关键字，表示一个占位符，能够保证程序的代码结构正确！
    # 程序运行时，pass 关键字不会执行任何的操作！
    else:
        print("你输入的不正确，请重新输入")
    # 01 ---- end
