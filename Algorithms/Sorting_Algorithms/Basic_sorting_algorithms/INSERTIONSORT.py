import random
def insertion_sort(A, first, last):
    for i in range(1, last+1):
        j = i - 1
        while j >= 0 and A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1
    return A



A = [random.randint(-1000, 1000) for i in range(50)]
insertion = insertion_sort(A, 0, len(A) - 1)

print(insertion)
print(insertion == sorted(A))