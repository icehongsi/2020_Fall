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

def fibo2(n):
    init_vector = np.array([1,1])
    mul = np.array([[1,1],[1,0]])
    for _ in range(n):
        init_vector = np.dot(mul, init_vector)
    print(init_vector[1])


n = int(input())

before = time.perf_counter()
fibo(n)
print("Time elapsed with 3 variables: ", time.perf_counter() - before)



before = time.perf_counter()
fibo2(n)
print("Time elapsed with numpy module: ", time.perf_counter() - before)