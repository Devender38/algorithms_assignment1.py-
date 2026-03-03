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

rec1_calls = 0
rec2_calls = 0


def rec1(n):
    global rec1_calls
    rec1_calls += 1

    if n <= 1:
        return 1
    return rec1(n//2) + n


def rec2(n):
    global rec2_calls
    rec2_calls += 1

    if n <= 1:
        return 1
    return rec2(n//2) + rec2(n//2) + n


def task4():

    sizes = [10, 50, 100]

    t1, t2 = [], []
    m1, m2 = [], []

    for n in sizes:

        global rec1_calls, rec2_calls

        rec1_calls = 0
        start = time.time()
        rec1(n)
        t1.append(time.time()-start)
        m1.append(measure_memory(rec1, n))

        rec2_calls = 0
        start = time.time()
        rec2(n)
        t2.append(time.time()-start)
        m2.append(measure_memory(rec2, n))

    plt.figure()
    plt.plot(sizes, t1, label="T(n)=T(n/2)+n")
    plt.plot(sizes, t2, label="T(n)=2T(n/2)+n")
    plt.title("Task 4 - Time Complexity")
    plt.xlabel("n")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(sizes, m1, label="T(n)=T(n/2)+n")
    plt.plot(sizes, m2, label="T(n)=2T(n/2)+n")
    plt.title("Task 4 - Space Complexity")
    plt.xlabel("n")
    plt.ylabel("Memory (KB)")
    plt.legend()
    plt.show()

print("Running Task 4...")
task4()