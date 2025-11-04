import logging
import pdb


logging.basicConfig(level=logging.INFO)


# def foo(s):
#     n = int(s)
#     assert n != 0, "n is zero!"
#     return 10 / n


# def main():
#     foo("0")


# main()

s = "0"
n = int(s)
pdb.set_trace()
logging.info(f"n = {n}")

print(10 / n)
