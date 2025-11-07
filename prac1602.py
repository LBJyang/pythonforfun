print("namedtuple**************************")
# namedtuple
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x)
print(p.y)
print(p)
isinstance(p, Point)
isinstance(p, tuple)

print("**************************\n")
print("deque**************************")
from collections import deque

q = deque(["a", "b", "c"])
q.append("x")
q.appendleft("y")
print(q)
isinstance(q, deque)
isinstance(q, list)
print("**************************\n")
print("OrderedDict**************************")
from collections import OrderedDict

d = dict([("a", 1), ("b", 2), ("c", 3)])
print(d)
od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
print(od)
od = OrderedDict()
od["z"] = 1
od["y"] = 2
od["x"] = 3
print(list(od.keys()))
print("**************************\n")
print("defaultdict**************************")
from collections import defaultdict

dd = defaultdict(lambda: "N/A")
dd["key1"] = "abc"
print(dd["key1"])
print(dd["key2"])
print("**************************\n")
print("Counter**************************")
from collections import Counter

c = Counter("programming")
print(c)
c.update("hello")
print(c)
print("**************************\n")
