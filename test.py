a = input("请输入一个正方形的边长：")
b = input("请输入长方形的长：")
c = input("请输入长方形的宽：")
# 计算正方形的面积
D = int(a) * int(a)
# 计算长方形面积
F = int(b) * int(c)
if D > F:
    print("正方形面积大！")
elif D < F:
    print("长方形面积大！")
else:
    print("正方形和长方形面积一样大！")
