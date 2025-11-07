import subprocess

# print("$ nslookup www.python.org")
# r = subprocess.call(["nslookup", "www.python.org"])
# print("Exit code:", r)

# print("$ nslookup")
# p = subprocess.Popen(
#     ["nslookup"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
# )
# output, err = p.communicate(b"set q=mx\npython.org\nexit\n")
# print(output.decode("utf-8"))
# print("Exit code:", p.returncode)
# import os

# print(f"Process {os.getpid()}")
# pid = os.fork()
# if pid == 0:
#     print(f"I am child process {os.getpid()} and my parent is {os.getppid()}")
# else:
#     print(f"I {os.getpid()} just created a child process {pid}")
from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print(f"Process to write:{os.getpid()}")
    for value in ["A", "B", "C"]:
        print(f"Put {value} to queue...")
        q.put(value)
        time.sleep(random.random())


def read(q):
    print(f"Process to read:{os.getpid()}")
    while True:
        value = q.get(True)
        print(f"Get {value} from queue.")


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
