from collections import OrderedDict


class FifoDict(OrderedDict):
    def __init__(self, capacity):
        super(FifoDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print("remove:", last)
        if containsKey:
            del self[key]
            print("set:", (key, value))
        else:
            print("add:", (key, value))
        return super().__setitem__(key, value)


n = FifoDict(3)
n["a"] = 1
n["b"] = 2
n["c"] = 3
print(n)
n["b"] = 4
print(n)
n["d"] = 5
print(n)
