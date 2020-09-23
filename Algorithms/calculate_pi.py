def long_add(A,B,C):
    pass
def long_sub(A,B,C):
    pass
def long_div(A,B,C):
    pass


P = int(input("Precision = ")) #sum of terms
L = P // 4 + 2
K = int(P/1.39894) + 1
w = v = q = pi = [0] * L
w[0], v[0] = 16*5, 4*239

for n in range(1, K+1):
    long_div(w, 5*5, w)
    long_div(v, 239*239, v)
    long_sub(w,v,q)
    long_div(q, 2*n-1, q)
    if n%2: long_add(pi, q, pi)
    else: long_sub(pi, q, pi)
print(pi)