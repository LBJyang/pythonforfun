import logging


def test():
    try:
        print("try...")
        r = 10 / int("2")
        print("result:", r)
    except ValueError as e:
        print("ValueError:", e)
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
    else:
        print("no error!")
    finally:
        print("finally...")
    print("END")


# test()


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar("0")
    except Exception as e:
        print("except:", e)
        # logging.exception(e)


# main()
# print("END")


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError(f"invalid value:{s}")
    return 10 / n


foo("0")
