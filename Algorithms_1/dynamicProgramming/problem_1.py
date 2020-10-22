def solution(n):
    a = [0, 1, 2]
    b = []
    for i in range(2, n+1):
        a.append(a[i-1] + a[i-2])
        b.append(a[-1] * 2)

    print(a[-1] + b[-2])

solution(3)

