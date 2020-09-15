def min_max2(A, left, right):
    if len(A) == 1:
        return A[left], A[left]
    elif len(A) == 2:
        return (A[left], A[right]) if A[left] < A[right] else (A[right], A[left])
    else: #when length of A is bigger than 2
        pivot = len(A)//2
        lower, upper = min_max2(A[left:pivot], 0, len(A[:pivot])-1), min_max2(A[pivot:], 0, len(A[pivot:])-1) # split into half - lower / upper
        temp_low = lower[0] if lower[0] < upper[0] else upper[0] # retrieve lowest value by comparison
        temp_high = upper[1] if lower[1] < upper[1] else lower[1] # retrieve HIGHEST value by comparison
        return temp_low, temp_high

a = list(map(int, input().split()))

m, M = min_max2(a, 0, len(a)-1)

print(m, M)