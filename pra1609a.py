from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print(f"Query info about {self.name}")


@contextmanager
def create_query(name):
    print("Begin")
    q = Query(name)
    yield q
    print("End")


with create_query("Bob") as q:
    q.query()
