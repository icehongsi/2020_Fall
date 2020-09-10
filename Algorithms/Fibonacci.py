def fibo(n):
    if n == 0: return 0
    prev, curr = 1, 1
    while n > 1:
        n -= 1
        temp = prev
        prev = curr
        curr = temp + curr
    return curr

print(fibo(int(input())))


def fibo2(n):
    return round((((1 + 5**0.5)/2)**n - ((1-5**0.5)/2)**n)/5**0.5)

print(fibo2(int(input())))
