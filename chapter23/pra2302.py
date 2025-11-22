import asyncio
import threading


async def hello(name):
    print(f"Hello,{name}!({threading.current_thread()})")
    await asyncio.sleep(1)
    print(f"Hello {name} again! ({threading.current_thread()})")
    return name


async def main():
    L = await asyncio.gather(hello("Alice"), hello("Bob"))
    print(L)


asyncio.run(main())
