# In Python, there are, in essence, three forms of concurrency:

# Multithreading — pre-emptive, via threading.
# Cooperative multitasking — via asyncio.
# Multiprocessing — via multiprocessing.

# The general advice is to use multiprocessing for CPU-bound problems
#  and multithreading/multitasking for I/O-bound problems

# ****** MULTIPROCESSING  *******
from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == "__main__":
    res = []
    with Pool(5) as p:  # 5 processes
        res.append(
            p.map(f, [1, 2, 3])
        )  # p.map(<func>, <iterable>) takes a function and an iterable,
        # As soon as a process is done with its current element from the iterable,
        # the process goes back to the iterable and grabs the next one to apply the function

print(res)


# ******* MULTITHREADING *******
# Threads are lightweight compared to processes and come with significantly less overhead


# mostly use
import concurrent.futures

def do_whatever(param_x):
    pass


param_list = ["p1", "p2", "p3", "pn"]

results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    rs = executor.map(do_whatever, param_list)
for idx, res in enumerate(rs):
    results.append(res)


# other example

from multiprocessing.pool import ThreadPool
import requests
from datetime import datetime

URL = "https://medium.fabianbosler.de/run"


def fetch_quote(*args):
    try:
        res = requests.get(URL).json()
    except Exception:
        res = "ERROR"


def parallel_extraction(threads, samples):
    start = datetime.now()
    res = []
    with ThreadPool(processes=threads) as pool:
        res.extend(pool.map(fetch_quote, range(samples)))
    return res, datetime.now() - start


if __name__ == "__main__":
    print(parallel_extraction(16, 64))

    # ****** MULTITASKING *********
# It’s different from multithreading and multiprocessing in a sense that it only
# uses one process and one thread but executes its code asynchronously.
# Those asynchronous routines can pause and wait for their result while handing over to other routines

from datetime import datetime
import aiohttp
import asyncio

URL = "https://medium.fabianbosler.de/run"


async def sample_asyncio(samples):
    start = datetime.now()

    async def main():
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as resp:
                return await resp.json()

    results = await asyncio.gather(*[main() for _ in range(sampels)])
    return results, datetime.now() - start


if __name__ == "__main__":
    print(asyncio.run(sample_asyncio(64))[1])
