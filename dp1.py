def solution(n):
    dp = [1, 2, 5]
    for i in range(3, n+1):
        dp.append(dp[i-1]*2 + dp[i-3])
    return dp[n-1]




def solution2(N):
        dp1 = [1, 1, 2]
        dp2 = [0, 0, 0]

        for i in range(3, N +1):
            temp = dp1[i-1] + dp1[i-2]
            dp2.append(dp2[i-1] + dp1[i-3] * 2)
            dp1.append(dp2[-1] + temp)
        return dp1[N] % (10**9 + 7)


print(solution(10))
print(solution2(10))