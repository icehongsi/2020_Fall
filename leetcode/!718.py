def findLength( A, B):
    def check(length):
        seen = {A[i:i+length] for i in range(len(A) - length + 1)} #A 리스트의 length 길이만큼의 subset을 만들어 seen에 저장
        print(seen)
        print(any(B[j:j+length] in seen for j in range(len(B) - length + 1)))
        return any(B[j:j+length] in seen for j in range(len(B) - length + 1)) #B 리스트의 subset을 각각 대입
    A = ''.join(map(chr, A)) #속도를 빠르게?
    B = ''.join(map(chr, B))
    lo, hi = 0, min(len(A), len(B)) + 1 #이진탐색 실행
    while lo < hi:
        mi = (lo + hi) // 2
        if check(mi):
            lo = mi + 1
        else:
            hi = mi
    return lo - 1

print(findLength([1,2,3,2,1], [3,2,1,4,7]))