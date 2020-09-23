def find_median_five(L):
    print(L)
    mid = len(L) // 2
    pivot = L[mid]
    S, M, B = [], [], []  # S >> values smaller than pivot / M >> values same as pivot / B >> values larger than pivot
    for num in range(len(L)):
        if L[num] < pivot:
            S.append(L[num])
        elif L[num] > pivot:
            B.append(L[num])
        else:  # L[num] == pivot:
            M.append(L[num])
    # print(S, B, M)
    # print(len(S), len(B), len(M), mid)
    if len(S) > mid:
        return find_median_five(S)
    elif len(S + M) < mid:
        return find_median_five(B)
    else:
        print(M)
        return M[0]
def MoM(L, k):  # L의 값 중에서 k번째로 작은 수 리턴
    if len(L) == 1:  # no more recursion
        return L[0]
    i = 0
    A, B, M, medians = [], [], [], []
    while i + 4 < len(L):
        medians.append(find_median_five(L[i: i + 5]))
        print("median list: ", medians)
        i += 5
    if i < len(L) and i + 4 >= len(L):
        medians.append(find_median_five(L[i:]))

    mom = MoM(medians, len(medians) // 2)
    for v in L:
        if v < mom:
            A.append(v)
        elif v > mom:
            B.append(v)
        else:
            M.append(v)

    if len(A) >= k:
        return MoM(A, k)
    elif len(A + M) <= k:
        return MoM(B, k - len(A + M))
    else:
        return mom


# n과 k를 입력의 첫 줄에서 읽어들인다
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
n, k = map(int, input().split())
L = list(map(int, input().split()))

print(n, k, L)
print(MoM(L, k))

#10 3
#-62 1 82 55 -48 63 47 -63 93 92