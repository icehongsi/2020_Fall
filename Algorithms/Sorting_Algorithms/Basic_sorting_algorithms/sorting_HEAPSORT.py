import time
import random
Hc, Hs = 0, 0
'''
def heap_sort(A):
    global Hc, Hs

    def heapify(i, limit = len(A)):  # function for heapify down, A[0] will always be the maximum value
        global Hc, Hs
        while (2 * i) + 1 < limit:
            Hc += 1
            L, R = (2 * i) + 1, (2 * i) + 2
            if L < limit and A[L] > A[i]:
                Hc += 1
                m = L
            else:
                Hc += 1
                m = i
            if R < limit and A[R] > A[m]:
                Hc += 1
                m = R
            if m != i:
                Hs += 1
                A[i], A[m] = A[m], A[i]
                i = m
            else:
                break

    for i in range(len(A) - 1, -1, -1):
        heapify(i)
    # Phase 1: Make an array that satisfies characteristics of Heap data structure

    for i in range(len(A) - 1, 0, -1): # Phase 2: switch A[0] and A[i] with for loop & heapify again
        A[0], A[i] = A[i], A[0]  # swap
        heapify(0, i - 1)

    return A
'''
Hc, Hs = 0, 0
def heap_sort(A):
    global Hc, Hs

    def heapify(i, limit=len(A)):  # function for heapify down, A[0] will always be the maximum value
        global Hc, Hs
        while (2 * i) + 1 < limit:
            Hc += 2
            L, R = (2 * i) + 1, (2 * i) + 2
            if L < limit and A[L] < A[i]:
                m = L
            else:
                m = i
            if R < limit and A[R] < A[m]:
                m = R
            if m != i:
                Hs += 1
                A[i], A[m] = A[m], A[i]
                i = m
            else:
                break

    for i in range(len(A) - 1, -1, -1):
        heapify(i)
    # Phase 1: Make an array that satisfies characteristics of Heap data structure

    for i in range(len(A) - 1, 0, -1):  # Phase 2: switch A[0] and A[i] with for loop & heapify again
        A[0], A[i] = A[i], A[0]  # swap
        heapify(0, i)
    Hs += len(A) - 2

    return A


print(heap_sort([3,1,2]))