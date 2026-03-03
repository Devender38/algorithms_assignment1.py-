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


fact_calls = 0
fib_calls = 0


def factorial(n):
    global fact_calls
    fact_calls += 1

    if n <= 1:
        return 1
    return n * factorial(n-1)


def fibonacci(n):
    global fib_calls
    fib_calls += 1

    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


@lru_cache(None)
def fibonacci_dp(n):
    if n <= 1:
        return n
    return fibonacci_dp(n-1) + fibonacci_dp(n-2)


def task3():

    sizes = [5, 10, 15]

    ft, rt, dt = [], [], []
    fm, rm, dm = [], [], []

    for n in sizes:

        global fact_calls, fib_calls

        fact_calls = 0
        start = time.time()
        factorial(n)
        ft.append(time.time()-start)
        fm.append(measure_memory(factorial, n))

        fib_calls = 0
        start = time.time()
        fibonacci(n)
        rt.append(time.time()-start)
        rm.append(measure_memory(fibonacci, n))

        start = time.time()
        fibonacci_dp(n)
        dt.append(time.time()-start)
        dm.append(measure_memory(fibonacci_dp, n))

    plt.figure()
    plt.plot(sizes, ft, label="Factorial")
    plt.plot(sizes, rt, label="Recursive Fibonacci")
    plt.plot(sizes, dt, label="DP Fibonacci")
    plt.title("Task 3 - Time Complexity")
    plt.xlabel("n")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(sizes, fm, label="Factorial")
    plt.plot(sizes, rm, label="Recursive Fibonacci")
    plt.plot(sizes, dm, label="DP Fibonacci")
    plt.title("Task 3 - Space Complexity")
    plt.xlabel("n")
    plt.ylabel("Memory (KB)")
    plt.legend()
    plt.show()

print("Running Task 3...")
task3()