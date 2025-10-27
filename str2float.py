from functools import reduce

DIGITS = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def str2float(s):
    point = False
    scale = 1

    def fn(x, y):
        nonlocal point, scale
        if y == ".":
            point = True
            return x
        x = 10 * x + DIGITS[y]
        if point:
            scale *= 10
        return x

    return reduce(fn, s, 0) / scale


print("str2float('123.456') =", str2float("123.456"))
if abs(str2float("123.456") - 123.456) < 0.00001:
    print("测试成功!")
else:
    print("测试失败!")
