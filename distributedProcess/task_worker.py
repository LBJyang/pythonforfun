import time, sys, queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

server_addr = "127.0.0.1"
print(f"Connect to server {server_addr}")
m = QueueManager(address=(server_addr, 5000), authkey=b"abc")
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()
for i in range(10):
    try:
        n = task.get(timeout=1)
        print(f"run task {n} * {n}")
        r = f"{n:d} * {n:d} = {n*n:d}"
        time.sleep(1)
        result.put(r)
    except queue.Queue.Empty:
        print("task queue is empty.")

print("worker exit")
