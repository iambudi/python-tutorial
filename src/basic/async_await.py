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
3. Asyncio is single-process and single-thread (event loop). It runs concurrently but not in parallel
=========================================================================================
asyncio.run() accepts awaitable object or object that can be used in an await expression.
Many asyncio APIs are designed to accept awaitables.
There are three main types of awaitable objects: coroutines, Tasks, and Futures.
Coroutines  : async def or await object
Tasks       : schedule coroutines concurrently (to run soon) using create_task.
Futures     : special low-level awaitable object. no need to use in app level.
=========================================================================================
Implementation:
Use create_task() when we want to start a background task or control over when to await the result
Use gather() when running multiple ops in concurrent and wait for all of them to complete
=========================================================================================
"""

import asyncio
import random
import time


async def calculate(x: int, y: int) -> int:
    # Simulate 1 second calculation
    await asyncio.sleep(1)
    return x * y


# create_task() is for scheduling a single coroutine to run as a Task.
async def run():
    # always use list, faster than tuple
    tasks = [asyncio.create_task(calculate(num, 10)) for num in range(1, 6)]

    # each tasks here will be run asynchronously
    print("Calculation started")
    for task in tasks:
        print("value from calc is {}".format(await task))
    print(f"{len(tasks)} tasks expected done in around 1 seconds")


# gather() is for running multiple awaitables concurrently and collecting their results.
def run_with_gather():
    async def task1(id: int):
        sleep_time_ms = random.randint(0, 1000)
        sleep_time_sec = sleep_time_ms / 1000
        print("task {} starting".format(id))
        await asyncio.sleep(sleep_time_sec)
        print("task {} finished".format(id))

    async def main():
        await asyncio.gather(task1(1), task1(2), task1(3))

    asyncio.run(main())


start = time.time()
asyncio.run(run())  # run() is awaitable func. Any object can use await means awaitable
end = time.time() - start
print("Elapsed time for running coroutine tasks %.2f seconds" % end)

run_with_gather()
