import base64


def safe_base64_decode(s):
    if len(s) % 4 != 0:
        temp = 4 - len(s) % 4
        s = s + temp * "="
    return base64.b64decode(s)


# 测试:
assert b"abcd" == safe_base64_decode("YWJjZA=="), safe_base64_decode("YWJjZA==")
assert b"abcd" == safe_base64_decode("YWJjZA"), safe_base64_decode("YWJjZA")
print("ok")
