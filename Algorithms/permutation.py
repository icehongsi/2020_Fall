def reconstruct(B):
    range(len(B)) B.pop()


B = [int(x) for x in input().split()]
A = reconstruct(B)

print(A)