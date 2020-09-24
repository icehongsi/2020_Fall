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