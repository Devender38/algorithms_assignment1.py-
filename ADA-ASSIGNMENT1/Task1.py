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


def constant(arr):
    return arr[0]

def linear(arr):
    s = 0
    for i in arr:
        s += i
    return s

def quadratic(arr):
    c = 0
    for i in arr:
        for j in arr:
            c += i + j
    return c

def logarithmic(n):
    while n > 1:
        n //= 2


def task1():
    sizes = [10, 100, 500, 1000]

    t1, t2, t3, t4 = [], [], [], []
    m1, m2, m3, m4 = [], [], [], []

    for n in sizes:

        arr = list(range(n))

        start = time.time()
        constant(arr)
        t1.append(time.time()-start)
        m1.append(measure_memory(constant, arr))

        start = time.time()
        linear(arr)
        t2.append(time.time()-start)
        m2.append(measure_memory(linear, arr))

        start = time.time()
        quadratic(arr)
        t3.append(time.time()-start)
        m3.append(measure_memory(quadratic, arr))

        start = time.time()
        logarithmic(n)
        t4.append(time.time()-start)
        m4.append(measure_memory(logarithmic, n))

    plt.figure()
    plt.plot(sizes, t1, label="O(1)")
    plt.plot(sizes, t2, label="O(n)")
    plt.plot(sizes, t3, label="O(n²)")
    plt.plot(sizes, t4, label="O(log n)")
    plt.title("Task 1 - Time Complexity")
    plt.xlabel("Input Size")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(sizes, m1, label="O(1)")
    plt.plot(sizes, m2, label="O(n)")
    plt.plot(sizes, m3, label="O(n²)")
    plt.plot(sizes, m4, label="O(log n)")
    plt.title("Task 1 - Space Complexity")
    plt.xlabel("Input Size")
    plt.ylabel("Memory (KB)")
    plt.legend()
    plt.show()

    print("Running Task 1...")
task1()