def find_median_five(L, k = None):
    if k is None:
        k = len(L)//2
    pivot = L[len(L)//2]
    S, M, B = [], [], []
    for i in range(len(L)):
        if L[i] < pivot: S.append(L[i])
        elif L[i] > pivot: B.append(L[i])
        else: M.append(L[i])
    if k < len(S):
        return find_median_five(S,k)
    elif k >= len(S) + len(M):
        return find_median_five(B, k-len(S)-len(M))
    else:
        return pivot







L = [2,4,5,1,3]
result = (find_median_five(L))
print("result: ", result)