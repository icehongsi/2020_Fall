import time, random


def evaluate_n2(A, x):
    result = 0  # initialize result variable
    for i in range(len(A)):  # iterate for len(A) times
        degree = 1  # initialize default x value as 1
        for j in range(i):
            degree *= x  # multiply x by iterating i times
        result += (A[i] * degree)  # multiply A[i] and degree, then add to the result
    return result  # return the result


# code for O(n^2)-time function

def evaluate_n(A, x):
    degree, result = 1, 0  # initialize degree and result
    for i in range(len(A)):
        result += (A[i] * degree)  # multiply A[i] and degree, then add to the result
        degree *= x  # multiply x to degree variable for every loop
    return result


# code for O(n)-time function

random.seed()  # random 함수 초기화
'''
A = [random.randint(-999, 999) for _ in range(len(input()))]
x = random.randint(-99, 99)

before = time.perf_counter()
evaluate_n2(A, x)
print(time.perf_counter() - before)

before = time.perf_counter()
evaluate_n(A, x)
print(time.perf_counter() - before)
'''
random.seed()  # random 함수 초기화
n, n1, n2 = [], [], []

for i in range(1000, 100000, 1000):
    print(i)
    A = [j for j in range(i)]
    x = 2
    before = time.perf_counter()
    evaluate_n2(A, x)
    elapsed_n2 = time.perf_counter() - before
    print("Time for n^2: ", elapsed_n2)
    before = time.perf_counter()
    evaluate_n(A, x)
    elapsed_n = time.perf_counter() - before
    print("Time for n: ", elapsed_n)

    n1.append(elapsed_n)
    n2.append(elapsed_n2)

    if elapsed_n2 > 60: break

print(n)
print(n1)
print(n2)
