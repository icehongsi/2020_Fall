import random
Qc, Qs = 0, 0
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
            left += 1; right -= 1
    A[first], A[right] = A[right], A[first]
    Qs += 1
    quick_sort(A, first, right - 1)
    quick_sort(A, right + 1, last)

    return A
