"""
=========================================================================================
asyncio is a library to write concurrent code using the async/await syntax. 
it is used as a foundation for multiple Python asynchronous frameworks 
that provide high-performance network and web-servers, database connection libraries, 
distributed task queues, etc.
=========================================================================================
⚠️ NOTE:
1. Adding `async` to a function or putting `await` expression won't make it 
automatically run concurrently
2. Concurrently will work when it's created as asyncio task object.
3. Asyncio is single-process and single-thread
=========================================================================================
asyncio.run() accepts awaitable object or object that can be used in an await expression. 
Many asyncio APIs are designed to accept awaitables.
There are three main types of awaitable objects: coroutines, Tasks, and Futures.
Coroutines  : async def or await object
Tasks       : schedule coroutines concurrently (to run soon) using create_task.     
Futures     : special low-level awaitable object. no need to use in app level.
=========================================================================================
"""
import asyncio
import time

start = time.time()

async def calculate(x: int, y: int) -> int:
    # Simulate 1 second calculation
    await asyncio.sleep(1)
    return x * y


async def run():
    # always use list, faster than tuple
    tasks = [asyncio.create_task(calculate(num, 10)) for num in range(1, 6)]

    # each tasks here will be run asynchronously
    print("Calculation started")
    for task in tasks:
        print("value from calc is {}".format(await task))
    print(f"{len(tasks)} tasks expected done in around 1 seconds")


asyncio.run(run())  # run() is awaitable func. Any object can use await means awaitable
end = time.time() - start
print("Elapsed time %.2f seconds" % end)
