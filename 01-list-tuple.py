# -*- coding: UTF-8 -*-

# Filename : 01-summation.py
# author by : （学员ID)

# 目的:
# 掌握基本的赋值，加减乘除运算，输入及输出方法
# 掌握 print 代入模式

# -------------------------------
# 练习一
# 关于列表的赋值操作示例
List1 =  ['张飞', '赵云', '马超', '吕布']

# 关于元组的赋值操作示例
tup1 = ('刘备', '曹操', '孙权')


# 关于列表的取值操作示例
pos = 0
value = List1[pos]
print("取出列表的第 %d 个 值，它是 %s" % (pos, value) )

print("--- 输出列表中所有元素")
pos = 0
for v in List1:
    print("取出列表的第 %d 个 值，它是 %s" % (pos, v) )
    pos = pos + 1

# 关于元组的取值操作示例
pos = 0
value = tup1[pos]
print("取出元组的第 %d 个 值，它是 %s" % (pos, value) )

print("--- 输出元组中所有元素")
pos = 0
for v in tup1:
    print("取出列表的第 %d 个 值，它是 %s" % (pos, v) )
    pos = pos + 1

# 关于列表的更新操作示例
newvalue = '关羽'
List1[0] = newvalue
print("--- 输出更新后的列表中所有元素")
pos = 0
for v in List1:
    print("取出列表的第 %d 个 值，它是 %s" % (pos, v) )
    pos = pos + 1