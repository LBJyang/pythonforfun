import random, time, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


def get_task_queue():
    return task_queue


def get_result_queue():
    return result_queue


QueueManager.register("get_task_queue", callable=get_task_queue)
QueueManager.register("get_result_queue", callable=get_result_queue)
if __name__ == "__main__":
    manager = QueueManager(address=("127.0.0.1", 5000), authkey=b"abc")
    manager.start()
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    for i in range(10):
        n = random.randint(0, 10000)
        print(f"Put task {n:d}")
        task.put(n)
    print("Try get results...")
    for i in range(10):
        r = result.get(timeout=10)
        print(f"Result:{r}")

    manager.shutdown()
    print("master exit.")
