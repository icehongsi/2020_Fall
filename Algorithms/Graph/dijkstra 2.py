import time

class Heap:
    def __init__(self, L=[]):
        self.A = L #weight 저장
        self.index = list(range(len(L))) #그래프에서의 원소 i가 힙의 몇 번째에 저장되어 있는지 저장
        print(self.index)
        # cf. self.index[3] >> 노드 3이 힙에 저장되어있는 위치
        self.make_heap()

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    def heapify_down(self, k, n):
        while 2 * k + 1 < n:
            L, R = 2 * k + 1, 2 * k + 2
            if L < n and self.A[L] < self.A[k]:
                m = L
            else:
                m = k
            if R < n and self.A[R] < self.A[m]:
                m = R
            if m != k:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                self.index[k], self.index[m] = self.index[m], self.index[k]
                k = m
            else:
                break

    def heapify_up(self, k):
        while k > 0 and self.A[(k - 1) // 2] > self.A[k]:
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            self.index[k], self.index[(k - 1) // 2] = self.index[(k - 1) // 2], self.index[k]
            k = (k - 1) // 2

    def make_heap(self):
        n = len(self.A)
        for k in range(n - 1, -1, -1):
            self.heapify_down(k, n)

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A) - 1)

    def delete_min(self):
        if len(self.A) == 0: return None  # 빈 리스트일 경우 아무것도 하지 않음
        key = self.A[0]  # 맨 처음 (제일 큰 값) 저장
        index = self.index[0]
        self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0]  # 처음과 마지막 바꾸기
        self.index[0], self.index[len(self.A) - 1] = self.index[len(self.A) - 1], self.index[0]
        self.A.pop()  # 실제로 리스트에서 delete!
        self.index.pop()
        self.heapify_down(0, len(self.A))  # len(self.A) = n-1
        return index, key

    def modify(self, idx, change_to):
        idx = self.index[idx] #힙에 저장되어 있는 위치 반환
        self.A[idx] = change_to
        self.heapify_up(idx)

    def get_node(self, idx):
        print(idx)
        print(self.A)
        print(self.index)
        idx = self.index[idx]
        return self.A[idx]

class Dijkstra:
    def __init__(self):
        n, e = int(input()), int(input())
        self.edge_matrix = [[0] * n for i in range(n)] # 1. 각 노드의 인접 노드를 저장할 행렬, i번째 열은 그래프 내 노드 번호와 인접한 노드를 의미함
        self.heap = Heap([0] + [1<<61] * (n-1)) # 2. weight를 저장할 리스트 (힙)
        self.weight = [0] + [1<<61] * (n-1) # 3. heap의 각 원소가 실제 몇 번 노드 번호인지 가리키는 리스트. Heap이 변경될 때마다 반영해야 함

        for i in range(e): # 모든 edge에 대해 입력받음
            col, row, weight = map(int, input().split())
            print(col, row, weight)
            self.edge_matrix[col][row] = weight
            print(self.edge_matrix)
        self.solution()

    def solution(self):
        while len(self.heap): # 힙에 원소가 있을 때까지 반복
            column, value = self.heap.delete_min()
            for terminal_node, weight in enumerate(self.edge_matrix[column]):
                if weight > 0:
                    print("terminal node and weight", terminal_node, weight)
                    if self.heap.get_node(terminal_node) > value + weight:
                        self.heap.modify(terminal_node, value + weight)
                        self.weight[terminal_node] = value + weight
        print(self.weight)

Dijkstra()