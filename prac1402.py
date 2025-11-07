# import time, threading


# def loop():
#     print(f"thread {threading.current_thread().name} is running...")
#     n = 0
#     while n < 5:
#         n = n + 1
#         print(f"thread {threading.current_thread().name} >>> {n}")
#         time.sleep(1)
#     print(f"thread {threading.current_thread().name} ended.")


# print(f"thread {threading.current_thread().name} is running...")
# t = threading.Thread(target=loop, name="LoopThread")
# t.start()
# t.join()
# print(f"thread {threading.current_thread().name} ended.")

# import time, threading

# balance = 0
# lock = threading.Lock()


# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n


# def run_thread(n):
#     for i in range(10000000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()


# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t2.join()
# print(balance)
import threading, multiprocessing


def loop():
    x = 0
    while True:
        x = x ^ 1
        if input("按q退出：") == "q":
            break


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
