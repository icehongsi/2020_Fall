import time
import random

'''
MERGE SORT - An sorting method that lowers its time complexity by selecting a pivot 'carefully'...
'''


def mergeSortedLists(A, first, last):
    mid = (first + last) // 2
    i, j, B = first, mid + 1, []
    while i <= mid and j <= last:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

    for k in range(i, mid+1):
        B.append(A[k])
    for k in range(j, last + 1):
        B.append(A[k])
    for i in range(first, last+1):
        A[i] = B[i-first]



def merge_sort(A, first, last):
    if first >= last: return
    mid = (first+last)//2
    merge_sort(A, first, mid)
    merge_sort(A, mid + 1, last)
    mergeSortedLists(A, first, last)
    return A

a = 2
while a <= 1<<20:
    a *= 2
    result = merge_sort([random.randint(-1000, 1000) for i in range(a)], 0, a-1)
    print(a, "SORT COMPLETED")