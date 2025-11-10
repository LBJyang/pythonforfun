class Query(object):
    def __init__(self, name):
        self.name = name
        print("I am initting...")

    def __enter__(self):
        print("entering...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Error")
        else:
            print("End")

    def query(self):
        print(f"Query info about {self.name}")


with Query("Bob") as q:
    q.query()
