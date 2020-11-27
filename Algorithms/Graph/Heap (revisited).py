class Heap:
    def __init__(self, L=[]):
        self.A = L

    def __str__(self):
        return str(self.A)

    def heapify_down(self, k, n):
        while 2 * k + 1 < n:
            L, R = 2 * k + 1, 2 * k + 2
            if L < n and self.A[L] > self.A[k]:
                m = L
            else:
                m = k
            if R < n and self.A[R] > self.A[m]:
                m = R
            if m != k:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break

    def make_heap(self):
        n = len(self.A)
        for k in range(n - 1, -1, -1):
            self.heapify_down(k, n)

    def heapify_up(self, k):
        while k > 0 and self.A[(k - 1) // 2] < self.A[k]:
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            k = (k - 1) // 2

    def insert(self, key):

        self.A.append(key)
        self.heapify_up(len(self.A) - 1)

    def delete_max(self):
        if len(self.A) == 0: return None  # 빈 리스트일 경우 아무것도 하지 않음
        key = self.A[0]  # 맨 처음 (제일 큰 값) 저장
        self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0]  # 처음과 마지막 바꾸기
        self.A.pop()  # 실제로 리스트에서 delete!
        self.heapify_down(0, len(self.A))  # len(self.A) = n-1
        return key

    def root(self):
        if self.A is None:
            return None
        return self.A[0]

    def elem(self):
        return len(self.A)