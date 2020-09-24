def reconstruct(B):
    result = []
    X = list(range(len(B)))
    for i in range(len(B)-1, -1, -1):
        result.append(X[B[i]])
        del X[B[i]]
    return list(reversed(result))



B = [int(x) for x in input().split()]
A = reconstruct(B)
print(A)

#reconstruct(range(10))