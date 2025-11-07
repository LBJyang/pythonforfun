# import re


# def is_valid_email(addr):
#     email_re = re.compile(r"^[a-zA-z\.\#]*\@[a-zA-Z]*\.com$")
#     if email_re.match(addr):
#         return True


# # 测试:
# assert is_valid_email("someone@gmail.com")
# assert is_valid_email("bill.gates@microsoft.com")
# assert not is_valid_email("bob#example.com")
# assert not is_valid_email("mr-bob@example.com")
# print("ok")

import re


def name_of_email(addr):
    email_re = re.compile(r"(?:<([a-zA-Z\s]*)>\s*)?([a-z]*)\@[a-zA-Z]*\.org$")
    m = email_re.match(addr)
    if m:
        return m.group(1) if m.group(1) else m.group(2)


# 测试:
assert name_of_email("<Tom Paris> tom@voyager.org") == "Tom Paris"
assert name_of_email("tom@voyager.org") == "tom"
print("ok")
