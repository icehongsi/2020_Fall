import random, timeit, sys

sys.setrecursionlimit(1 << 15)


##
## 여기에 세 가지 정렬함수를 위한 코드를...
##
def insertion_sort(A, first, last):
    for i in range(1, last + 1):
        j = i - 1
        while j >= 0 and A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            j -= 1
    return A


def quick_sort(A, first, last):
    global Qc, Qs
    if first >= last:
        return
    elif 10 <= last - first <= 40:  # insertion sort
        for i in range(1, last + 1):
            j = i - 1
            while j >= 0 and A[j] > A[j + 1]:
                Qc += 1
                Qs += 1
                A[j], A[j + 1] = A[j + 1], A[j]
                j -= 1
        return
    Qc += 1
    left, right = first + 1, last
    pivot = A[first]
    while left <= right:
        Qc += 1
        while left <= last and A[left] < pivot:
            Qc += 1
            left += 1
        while right > first and A[right] > pivot:
            Qc += 1
            right -= 1
        if left <= right:
            Qc += 1
            A[left], A[right] = A[right], A[left]
            Qs += 1
            left += 1;
            right -= 1
    A[first], A[right] = A[right], A[first]
    Qs += 1
    quick_sort(A, first, right - 1)
    quick_sort(A, right + 1, last)

    return A


def mergeSortedLists(A, first, last):
    global Mc, Ms
    mid = (first + last) // 2
    i, j, B = first, mid + 1, []
    while i <= mid and j <= last:
        Mc += 2
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
    Ms += (last - first)


def merge_sort(A, first, last):
    global Mc, Ms
    Mc += 1
    if first >= last:
        return
    elif 10 <= last - first <= 40:
        for i in range(1, last + 1):
            j = i - 1
            while j >= 0 and A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                Mc += 1
                Ms += 1
                j -= 1
        return A
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
            Hc += 2
            L, R = (2 * i) + 1, (2 * i) + 2
            if L < limit and A[L] > A[i]:
                m = L
            else:
                m = i
            if R < limit and A[R] > A[m]:
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


# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#


def check_sorted(A):
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            return False
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
A = quick_sort(A, 0, len(A) - 1)
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Merge sort:")
B = merge_sort(B, 0, len(A) - 1)
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
C = heap_sort(C)
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

print(A, B, C, sep="\n")

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert (check_sorted(A))
assert (check_sorted(B))
assert (check_sorted(C))

num, count = 0, 100
import pandas
time_counted = min()
while count <= 500000:
    Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
    time_counted.loc[num, 'n'] = count  # number of num
    random.seed()
    A = []
    for i in range(count):
        A.append(random.randint(-1000, 1000))
    B = A[:]
    C = A[:]
    print("num += ")
    print("Quick sort:")

    time_counted.loc[num, 'Qt'] = timeit.timeit("quick_sort(A, 0, len(A) - 1)", globals=globals(), number=1)
    print("time =", time_counted.loc[num, 'n'])
    A = quick_sort(A, 0, len(A) - 1)
    print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
    time_counted.loc[num, 'Qc'] = Qc
    time_counted.loc[num, 'Qs'] = Qs

    print("Merge sort:")
    B = merge_sort(B, 0, len(A) - 1)
    time_counted.loc[num, 'Mt'] = timeit.timeit("merge_sort(B, 0, len(B) - 1)", globals=globals(), number=1)
    print("time =", timeit.timeit(time_counted, loc[num, 'Mt']))

    print("comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))
    time_counted.loc[num, 'Mc'] = Mc
    time_counted.loc[num, 'Ms'] = Ms

    print("Heap sort:")
    time_counted.loc[num, 'Ht'] = timeit.timeit("heap_sort(C)")
    print("time =", timeit.timeit(time_counted.loc[num, 'Ht'])
    C = heap_sort(C)
    print("comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

    time_counted.loc[num, 'Mc'] = Mc
    time_counted.loc[num, 'Ms'] = Ms

    print(A, B, C, sep="\n")

    # 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
    assert (check_sorted(A))
    assert (check_sorted(B))
    assert (check_sorted(C))

    if num % 2 == 0:
        count *= 5
    else:
        count *= 2
    num += 1