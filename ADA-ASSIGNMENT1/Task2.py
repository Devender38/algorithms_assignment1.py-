import time
import random
import matplotlib.pyplot as plt
import tracemalloc
from functools import lru_cache

def measure_memory(func, *args):
    tracemalloc.start()
    func(*args)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024


def linear_search(arr, key):
    for i in arr:
        if i == key:
            return True
    return False

def binary_search(arr, key):
    l, h = 0, len(arr)-1

    while l <= h:
        m = (l+h)//2

        if arr[m] == key:
            return True
        elif arr[m] < key:
            l = m+1
        else:
            h = m-1
    return False


def task2():

    sizes = [100, 500, 1000, 2000]

    lt, bt = [], []
    lm, bm = [], []

    for n in sizes:

        arr = sorted(random.sample(range(1, n*5), n))
        key = arr[-1]

        start = time.time()
        linear_search(arr, key)
        lt.append(time.time()-start)
        lm.append(measure_memory(linear_search, arr, key))

        start = time.time()
        binary_search(arr, key)
        bt.append(time.time()-start)
        bm.append(measure_memory(binary_search, arr, key))

    plt.figure()
    plt.plot(sizes, lt, label="Linear Search")
    plt.plot(sizes, bt, label="Binary Search")
    plt.title("Task 2 - Time Complexity")
    plt.xlabel("Input Size")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(sizes, lm, label="Linear Search")
    plt.plot(sizes, bm, label="Binary Search")
    plt.title("Task 2 - Space Complexity")
    plt.xlabel("Input Size")
    plt.ylabel("Memory (KB)")
    plt.legend()
    plt.show()

print("Running Task 2...")
task2()