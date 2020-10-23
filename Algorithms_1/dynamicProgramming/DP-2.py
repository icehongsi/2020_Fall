def solution(chars, n):
    dp = [[0 for char in chars] for char in chars]
    for char in range(len(chars)):
        dp[char][char] = len(chars[char])
    result = 0
    for i in range(len(chars)):
        for j in range(i+1, len(chars)):
            temp = dp[i][j-1] + len(chars[j]) + 1
            if temp <= n:
                dp[i][j] = temp
                print(dp)
            else:
                break

solution("ape eats apple cider a lot.".split(), 8)