#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"a test module"

__author__ = "yangfan"


import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello,world!")
    elif len(args) == 2:
        print(f"Hello,{args[1]}")
    else:
        print("too many arguments!")


if __name__ == "__main__":
    test()
