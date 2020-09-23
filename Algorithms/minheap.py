def QuickSelect(L):
    print("L: ", L)
    mid = len(L)//2
    pivot = L[mid]
    S, M, B = [], [], []  # S >> values smaller than pivot / M >> values same as pivot / B >> values larger than pivot
    for num in range(len(L)):
        if L[num] < pivot:
            S.append(L[num])
        elif L[num] > pivot:
            B.append(L[num])
        else:  # L[num] == pivot:
            M.append(L[num])
    print(S, B, M)
    print(len(S), len(B), len(M), mid)
    if len(S) > mid:
        print("len(S) >= mid")
        return QuickSelect(S)
    elif len(S + M) < mid:
        print("len(S + B) < mid")
        return QuickSelect(B)
    else:
        return M[0]
L = [-62, 1, 82, 55, -48]
result = QuickSelect(L)
print(result)