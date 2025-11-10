# import itertools

# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))
# # for n in natuals:
# #     print(n)

# # cs = itertools.cycle("ABC")
# # for c in cs:
# #     print(c)

# # ns = itertools.repeat("A", 3)
# # for n in ns:
# #     print(n)

# # for c in itertools.chain("ABC", "XYZ"):
# #     print(c)
# for key, group in itertools.groupby("AaaBbCcCAaaa", lambda c: c.upper()):
#     print(key, list(group))

import itertools


def pi(N):
    "计算pi的值"
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odds = itertools.islice(itertools.count(1, 2), N)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    terms = ((-1 if i % 2 else 1) * 4 / o for i, o in enumerate(odds))
    # step 4: 求和:
    return sum(terms)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print("ok")
