'''
[DP] Tiling with I and L dominoes제출완료
50점
2xn 판을 I자 모양 도미노와 L자 모양 도미노로 채우는 경우의 수를 계산해 출력한다
두 가지 모양의 도미노는 충분히 많아서 원하는 만큼 사용할 수 있다고 가정
도미노를 원하는 각도 (90, 180, 270)로 회전하고 상하좌우 대칭을 자유롭게 해서 배치 가능
입력: n   # 2xn 판을 의미
출력: 두 가지 모양의 도미노로 채울 수 있는 경우의 수 (자연수)
분석: 코드 마지막 부분에 주석으로 본인이 세운 점화식을 쓰고 간략히 설명할 것
예: 아래 그림은 2x3 판을 채우는 다섯가지 경우를 나타낸다
힌트1: 가장 오른쪽에 도미노를 배치하고 그 왼쪽 부분에 대한 경우의 수를 DP 테이블의 값으로 표현해서 DP 점화식을 세워본다
힌트2: DP 테이블이 2개 필요하다
'''

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