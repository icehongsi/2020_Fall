import random
'''
QUICKSORT ALGORITHM
'''

def quickSort_notInPlace(A, first, last): #A: list
    if last - first < 1 : return
    pivot, S, M, L = A[0], [], [], []
    for elem in A[first:last+1]:
        if pivot > elem: S.append(elem)
        elif pivot < elem: L.append(elem)
        else: M.append(elem)
    return quickSort_notInPlace(S, 0, len(S) - 1) + M + quickSort_notInPlace(L, 0, len(L) - 1)


def quick_sort(A, first, last):
    if first >= last: return A
    left, right = first + 1, last
    pivot = A[first]
    while left <= right:
        while left <= last and A[left] < pivot:
            left += 1
        while right > first and A[right] > pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1; right -= 1
    A[first], A[right] = A[right], A[first]
    quick_sort(A, first, right - 1)
    quick_sort(A, right + 1, last)

    return A


a = 2
while a <= 1<<20:
    a *= 2
    result = quick_sort([random.randint(-1000, 1000) for i in range(a)], 0, a-1)
    print(a, "SORT COMPLETED")