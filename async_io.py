import threading
import asyncio

a = 0
@asyncio.coroutine
def hello():
    global a
    print('Hello world! (%s)' % threading.currentThread())
    print(a)
    a += 1
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()