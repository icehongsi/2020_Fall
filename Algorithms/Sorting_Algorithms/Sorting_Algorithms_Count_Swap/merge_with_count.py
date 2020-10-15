import random
Mc, Ms = 0, 0
def mergeSortedLists(A, first, last):
    global Mc, Ms
    mid = (first + last) // 2
    i, j, B = first, mid + 1, []
    while i <= mid and j <= last:
        Mc += 1
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
        Ms += 1

def merge_sort(A, first, last):
    global Mc, Ms
    if first >= last: return
    mid = (first+last)//2
    merge_sort(A, first, mid)
    merge_sort(A, mid + 1, last)
    mergeSortedLists(A, first, last)
    return A



a = 2
while a <= 1<<15:
    a *= 2
    result = merge_sort([random.randint(-1000, 1000) for i in range(a)], 0, a-1)
    print(a, "SORT COMPLETED")