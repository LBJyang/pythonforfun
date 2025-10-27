import functools


def log(arg=None):
    if callable(arg):
        func = arg

        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(f"call {func.__name__}")
            return func(*args, **kw)

        return wrapper

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(f"{arg} {func.__name__}")
            return func(*args, **kw)

        return wrapper

    return decorator


@log
def f1():
    print("f1 running")


@log("execute")
def f2():
    print("f2 running")


f1()
f2()
