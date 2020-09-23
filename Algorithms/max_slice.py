def max_slice(A):
    if len(A) == 1:
        return A[0]
    return max(max_slice(A[:len(A)-1]), A[n-1])