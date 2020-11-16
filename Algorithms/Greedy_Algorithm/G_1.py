def pin(A):
    pin_loc, count = -1, 0
    for i in range(len(A)):
        if A[i][0] > pin_loc:
            count += 1
            pin_loc = A[i][1]
            print(A[i-1])
            print(A[i])
            print(pin_loc)
    return count




A = []
for i in range(int(input())):
    A.append(tuple(
        map(int, input().split())
    ))

A.sort(key = lambda x: x[1])
print(A)
print(pin(A))
