def min_max2(A):
    if len(A) == 1:
        return A[0], A[0]
    elif len(A) == 2:
        return (A[0], A[1]) if A[0] < A[1] else (A[1], A[0])
    else: #when length of A is bigger than 2
        pivot = len(A)//2
        lower, upper = min_max2(A[:pivot]), min_max2(A[pivot:]) # split into half - lower / upper
        temp_low = lower[0] if lower[0] < upper[0] else upper[0] # retrieve lowest value by comparison
        temp_high = upper[1] if lower[1] < upper[1] else lower[1] # retrieve HIGHEST value by comparison
        return temp_low, temp_high

a = list(map(int, input().split()))

m, M = min_max2(a)

print(m, M)