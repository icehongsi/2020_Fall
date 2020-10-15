# coding=utf-8
import random, timeit
import pandas as pd


##
# 여기에 세 가지 정렬함수를 위한 코드를...
##

def quick_sort(A, first, last):
    global Qc, Qs
    if first >= last: return A
    left, right = first + 1, last
    pivot = A[first]
    while left <= right:
        init_left, init_right = left, right
        while left <= last and A[left] < pivot:
            left += 1
        while right > first and A[right] > pivot:
            right -= 1
        Qc += (left + right - init_left - init_right + 1)
        if left <= right:
            A[left], A[right] = A[right], A[left]
            Qs += 1
            left += 1;
            right -= 1
    A[first], A[right] = A[right], A[first]
    Qs += 1
    quick_sort(A, first, right - 1)
    quick_sort(A, right + 1, last)

    return A


'''
merge_sort에 대한 각주 - 배열의 원소 개수가 10 - 40 사이의 값일 경우 merge sort 대신 insertion sort을 활용하여 하이브리드 정렬을 하는 것이 효율적을 보여지나,
아래의 경우는 비교 및 교환횟수를 계산하는 기본연산의 횟수가 필요 이상으로 많아져 수행시간이 오래 걸리는 결과를 초래하였기 때문에 merge_sort만 이용하여 정렬되도록 하였습니다.
'''


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

    for k in range(i, mid + 1):
        B.append(A[k])
    for k in range(j, last + 1):
        B.append(A[k])
    for i in range(first, last + 1):
        A[i] = B[i - first]
        Ms += 1

def merge_sort(A, first, last):
    global Mc, Ms
    if first >= last: return
    mid = (first + last) // 2
    merge_sort(A, first, mid)
    merge_sort(A, mid + 1, last)
    mergeSortedLists(A, first, last)
    return A


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


# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
    for i in range(n - 1):
        if A[i] > A[i + 1]: return False
    return True


#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000, 1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert (check_sorted(A))
assert (check_sorted(B))
assert (check_sorted(C))
