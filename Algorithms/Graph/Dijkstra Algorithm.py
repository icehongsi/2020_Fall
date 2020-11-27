import heapq
class Dijkstra:
    def __init__(self):
        n, e = int(input()), int(input())
        self.edge_matrix = [[0] * n for i in range(n)] # 1. 각 노드의 인접 노드를 저장할 행렬, i번째 열은 그래프 내 노드 번호와 인접한 노드를 의미함
        # 2. weight를 저장할 리스트 (힙)
        self.weight = [0] + [1<<61] * (n-1) # 3. heap의 각 원소가 실제 몇 번 노드 번호인지 가리키는 리스트. Heap이 변경될 때마다 반영해야 함
        self.heap = []

        for i in range(n): # heap 만들기
            heapq.heappush(self.heap, [self.weight[i], i])

        for i in range(e): # 모든 edge에 대해 입력받음 - 인접행렬 활용
            col, row, weight = map(int, input().split())
            self.edge_matrix[col][row] = weight
        self.solution()

    def getIndex(self, idx):
        for index, value in enumerate(self.heap):
            if value[1] == idx:
                return index

    def decreaseKey(self, idx, change_to):
        idx = self.getIndex(idx)
        if idx != None:
            self.heap[idx][0] = change_to


    def solution(self):
        while len(self.heap): # 힙에 원소가 있을 때까지 반복
            heapq.heapify(self.heap)
            min_weight, index = heapq.heappop(self.heap)
            for terminal_node, weight in enumerate(self.edge_matrix[index]):
                if weight > 0:
                    if self.weight[terminal_node] > weight + min_weight:
                        self.weight[terminal_node] = weight + min_weight
                        self.decreaseKey(terminal_node, weight + min_weight)
        self.printSolution()

    def printSolution(self):
        for i in range(len(self.weight)):
            if self.weight[i] == 1<<61:
                print("inf", end = " ")
            else:
                print(self.weight[i], end = " ")

Dijkstra()