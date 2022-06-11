import threading
import concurrent.futures
import time
from random import randint
from typing import List

"""
Multi Threading (MT) and Multi Process (MP)
"""


class Computation:
    def compute(self, delay: float) -> float:
        time.sleep(delay)  # assume long_process
        print(randint(1000, 9999))
        return delay

    def compute_mt(self) -> threading.Thread:
        # create a new thread which target func will need to run
        # it will start in different thread of control
        wait = 1.2
        # pass argument
        th = threading.Thread(target=self.compute, name="calculation", args=[wait])
        th.start()
        return th

    def compute_pool(self):
        # this make it easier to use thread. it does not require to import threading
        # using context manager with Thread Pool
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            delays = reversed([1, 2, 3, 4, 5])
            # dont call comput() just give it as func arg with a parameter
            # results = [executor.submit(self.compute, delay) for delay in delays]
            # for f in concurrent.futures.as_completed(results):
            #     print(f.result())
            results = executor.map(self.compute, delays)
            for result in results:
                print(result)


# Without MT this will run in a sequence.
# Next loop will run after previous done
start = time.perf_counter()
for _ in list(range(3)):
    Computation().compute(1)
finish = time.perf_counter()
print(f"Without MT tooks {round(finish - start,2)} secs")

# With MT as soon as fun call waiting It will call next.
# It does not actually run simultaneously
# It just gives illusion of running simultaneously
start = time.perf_counter()
threads: List[threading.Thread] = []
for _ in range(3):
    threads.append(Computation().compute_mt())

# .join method will wait all the thread (with join()) terminates
# So it's easier to measure the elapsed time
for thread in threads:
    thread.join()
finish = time.perf_counter()
print(f"With MT tooks {round(finish - start,2)} secs")

# Threadpool
start = time.perf_counter()
Computation().compute_pool()
finish = time.perf_counter()
print(f"With Thread Pool tooks {round(finish - start,2)} secs")
