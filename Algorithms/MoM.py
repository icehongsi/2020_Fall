import time

def find_median_five(L):

    return sorted(L)[len(L)//2]

def MoM(L, k): #L번째 수 중 k번째로 작은 수 돌려주기
    if len(L) == 1: return L[0]
    i = 0; A, B, M, medians = [], [], [], []
    while i+4 < len(L):
        medians.append(find_median_five(L[i: i+5]))
        # find medians and add values into median array
        i += 5
    if i < len(L) and i+4 >= len(L): #마지막 조각
        medians.append(find_median_five(L[i:]))
    mom = MoM(medians, len(medians)//2) # "median of medians"
    print("median of medians: ", mom)
    for v in L:
        #print(v, end = "")
        if v < mom:
            A.append(v)
        elif v > mom:
            B.append(v)
        else:
            M.append(v)
    print(A, B, M)
    if len(A) >= k:
        print("option 1")
        return MoM(A, k)
    elif len(A + M) < k:
        print("option 2")
        return MoM(B, k - len(A+M))
    else:
        print("option 3")
        return mom


x = "38 19 5 97 42 -58 -68 -99 66 -52 5 72 57 66 -96 67 78 15 -31 73"


L = list(map(int, x.split()))
#L = list(map(int, input().split()))
#k = int(input())
k = 10
print(MoM(L, k))

'''
10 3
-62 1 82 55 -48 63 47 -63 93 92
'''