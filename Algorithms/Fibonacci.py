import numpy as np
import time


def fibo(n):
    if n == 0: return 0
    prev, curr = 1, 1
    while n > 1:
        n -= 1
        temp = prev
        prev = curr
        curr = temp + curr
    print(curr)


def fibo2(n):  # by power of matrix, logarithmic growth
    init_vector = np.array([1, 1])
    mul = np.array([[1, 1], [1, 0]])
    print(np.linalg.matrix_power(mul, n)[0])


def fibo3(n):  # extremely inefficient algorithm (exponential growth)
    if n <= 1: return n
    return fibo3(n - 1), fibo3(n - 2)

n = int(input())

before = time.perf_counter()
fibo(n)
print("Time elapsed with 3 variables: ", time.perf_counter() - before)

before = time.perf_counter()
fibo2(n)
print("Time elapsed with numpy module: ", time.perf_counter() - before)
