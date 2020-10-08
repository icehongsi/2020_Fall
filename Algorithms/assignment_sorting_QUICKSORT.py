import random
'''
QUICKSORT ALGORITHM
'''

def quickSort(A): #A: list
    if len(A) < 2 : return A
    pivot, S, M, L = A[0], [], [], []
    for elem in A:
        if pivot > elem: S.append(elem)
        elif pivot < elem: L.append(elem)
        else: M.append(elem)
    return quickSort(S) + M + quickSort(L)



A = [random.randint(-1000, 1000) for i in range(10)]
by_quicksort = quickSort(A)
by_function = sorted(A)


print(by_quicksort, by_function, sep = "\n")