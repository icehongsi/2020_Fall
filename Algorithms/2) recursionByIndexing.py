def min_max(A):
    if len(A) == 1: return A[0], A[0]
    lower, upper = min_max(A[:len(A)//2]), min_max(A[len(A)//2:])
    return (lower[0] if lower[0] < upper[0] else upper[0], upper[1] if lower[1] < upper[1] else lower[1])


#a = list(map(int, input().split()))
a = [3,4,1,5,2]
m, M = min_max(a)
print(m, M)