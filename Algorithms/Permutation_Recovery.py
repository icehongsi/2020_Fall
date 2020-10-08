def reconstruct(B):
    result, X = [], list(range(len(B)))
    for i in range(len(B) - 1, -1, -1):
        result.append(X[B[i]])
        X[B[i]] = X[B[i + 1]]
    return list(reversed(result))


# B로부터 A를 재구성해 리턴
# 이 함수를 작성합니다~


B = [int(x) for x in input().split()]
A = reconstruct(B)
print(A)