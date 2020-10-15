import time
import random
Hc, Hs = 0, 0

def heap_sort(A):
    global Hc, Hs
    def heapify(i, limit=len(A)):  # function for heapify down, A[0] will always be the maximum value
        global Hc, Hs
        while (2 * i) + 1 < limit:
            L, R = (2 * i) + 1, (2 * i) + 2
            if L < limit and A[L] > A[i]:
                m = L
            else:
                m = i
            if R < limit and A[R] > A[m]:
                m = R
            Hc += 2
            if m != i:
                A[i], A[m] = A[m], A[i]
                Hs += 1
                i = m
            else:
                break

    for i in range(len(A) - 1, -1, -1):
        heapify(i)
    # Phase 1: Make an array that satisfies characteristics of Heap data structure

    for i in range(len(A) - 1, 0, -1):  # Phase 2: switch A[0] and A[i] with for loop & heapify again
        A[0], A[i] = A[i], A[0]  # swap
        Hs += 1
        heapify(0, i)

    return A


a = 2
while a <= 1<<20:
    a *= 2
    result = heap_sort([random.randint(-1000, 1000) for i in range(a)])
    print(a, "SORT COMPLETED")