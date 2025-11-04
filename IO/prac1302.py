from io import BytesIO, StringIO


def main():
    f = StringIO()
    f.write("hello")
    f.write(" ")
    f.write("world!")
    print(f.getvalue())


def test():
    f = StringIO("Hello!\nHi!\nGoodbye!")
    while True:
        s = f.readline()
        if s == "":
            break
        print(s.strip())


def mainbytes():
    f = BytesIO()
    f.write("中文".encode("utf-8"))
    print(f.getvalue())


def testbytes():
    f = BytesIO(b"\xe4\xb8\xad\xe6\x96\x87")
    print(f.read().decode())


testbytes()

# mainbytes()
# test()

# main()
