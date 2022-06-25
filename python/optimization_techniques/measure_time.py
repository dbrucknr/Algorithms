"""Example of Measuring Time Perfomance Metric for a single run time"""
from time import perf_counter


def upto_for_loop(n):
    total = 0
    for i in range(n):
        total += 1
    return total


def upto_sum_method(n):
    return sum(range(n))


if __name__ == "__main__":
    n = 1_000_000

    start = perf_counter()
    upto_for_loop(n)
    duration = perf_counter() - start
    print("for loop performance:", duration)

    start = perf_counter()
    upto_sum_method(n)
    duration = perf_counter() - start
    print("sum method performance:", duration)
