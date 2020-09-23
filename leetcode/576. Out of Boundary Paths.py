def findPaths(m, n, N, i, j):
    matrix = ([(p, q, abs(i - p) + abs(j - q)) for q in range(n) for p in range(m)]) #column
    print(matrix) # element is a tuple: row / col / cost
    result = 0
    for step in range(N):
        print("Step:", step)
        for i in matrix:
            if i[2] <= N and step%2 == i[2] % 2:
                print(i)
                print((i[0] == 0, i[0] == m-1, i[1] == 0, i[1] == n-1).count(True))
                result += (i[0] == 0, i[0] == m-1, i[1] == 0, i[1] == n-1).count(True)

    print(result)
    #matrix = list(filter(lambda x: x[2] <= N, matrix))


findPaths(1,3,3,0,1)