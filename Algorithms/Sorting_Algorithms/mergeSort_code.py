import random

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

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
while a <= 1<<15:
    a *= 2
    result = merge_sort([random.randint(-100, 100) for i in range(a)])
    print(a, "SORT COMPLETED")