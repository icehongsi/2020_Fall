def getMaxInterval(array):
    DP = array[0] + [1<<64] * (len(array)-1)
    max_value = array[0]
    for i in range(1, array):
        DP[i] = max(DP[i-1] + DP[i], DP[i])
        if DP[i] > max_value:
            max_value = DP[i]
    
    print(max_value)


getMaxInterval(list(map(int, input().split())))