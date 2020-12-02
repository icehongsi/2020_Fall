import heapq
class Dijkstra:
    def __init__(self):
        n, e = int(input()), int(input())
        self.edge_linked_list = {} # 1. 각 노드의 인접 노드를 저장할 행렬, i번째 열은 그래프 내 노드 번호와 인접한 노드를 의미함
        # 2. weight를 저장할 리스트 (힙)
        self.weight = [0] + [1<<61] * (n-1) # 3. heap의 각 원소가 실제 몇 번 노드 번호인지 가리키는 리스트. Heap이 변경될 때마다 반영해야 함
        self.heap = []

        for i in range(n): # heap 만들기
            heapq.heappush(self.heap, [self.weight[i], i])

        for i in range(e): # 모든 edge에 대해 입력받음 - 인접행렬 활용
            initial_node, terminal_node, weight = map(int, input().split())
            if initial_node in self.edge_linked_list:
                self.edge_linked_list[initial_node].append([terminal_node, weight])
            else:
                self.edge_linked_list[initial_node] = [[terminal_node, weight]]
        self.solution()

    def getIndex(self, idx):
        for index, value in enumerate(self.heap):
            if value[1] == idx:
                return index

    def decreaseKey(self, decrease_key_list):
        for index in range(len(self.heap)):
            if self.heap[index][1] in decrease_key_list:
                self.heap[index][0] = decrease_key_list[self.heap[index][1]]
            if decrease_key_list == None:
                return


    def solution(self):
        while len(self.heap): # 힙에 원소가 있을 때까지 반복
            heapq.heapify(self.heap)
            min_weight, index = heapq.heappop(self.heap)
            if index in self.edge_linked_list:
                decrease_key_list = {}
                for terminal_node, weight in self.edge_linked_list[index]:
                    if self.weight[terminal_node] > weight + min_weight:
                            self.weight[terminal_node] = weight + min_weight # self.weight 조정
                            decrease_key_list[terminal_node] = weight + min_weight # heap 조정
                self.decreaseKey(decrease_key_list)
        self.printSolution()

    def printSolution(self):
        for i in range(len(self.weight)):
            if self.weight[i] == 1<<61:
                print("inf", end = " ")
            else:
                print(self.weight[i], end = " ")

Dijkstra()

'''
{0: [[1, 5], [2, 8], [3, 1], [4, 3]], 9: [[3, 3]], 1: [[2, 8]], 3: [[4, 8], [9, 6], [2, 8]], 2: [[4, 5]], 6: [[3, 7]], 4: [[0, 4], [2, 1]], 8: [[0, 1]]}
[[0, 0], [2305843009213693952, 1], [2305843009213693952, 2], [2305843009213693952, 3], [2305843009213693952, 4], [2305843009213693952, 5], [2305843009213693952, 6], [2305843009213693952, 7], [2305843009213693952, 8], [2305843009213693952, 9]]
1 5
2 8
3 1
4 3
[[2, 1], [4, 3], [3, 2], [2305843009213693952, 7], [2305843009213693952, 4], [2305843009213693952, 5], [2305843009213693952, 6], [2305843009213693952, 9], [2305843009213693952, 8]]
2 8
[[3, 2], [4, 3], [2305843009213693952, 5], [2305843009213693952, 7], [2305843009213693952, 4], [2305843009213693952, 8], [2305843009213693952, 6], [2305843009213693952, 9]]
4 5
[[4, 3], [2305843009213693952, 4], [2305843009213693952, 5], [2305843009213693952, 7], [2305843009213693952, 9], [2305843009213693952, 8], [2305843009213693952, 6]]
4 8
9 6
2 8
[[2305843009213693952, 4], [2305843009213693952, 6], [2305843009213693952, 5], [2305843009213693952, 7], [2305843009213693952, 9], [2305843009213693952, 8]]
0 4
2 1
[[2305843009213693952, 5], [2305843009213693952, 6], [2305843009213693952, 8], [2305843009213693952, 7], [2305843009213693952, 9]]
[[2305843009213693952, 6], [2305843009213693952, 7], [2305843009213693952, 8], [2305843009213693952, 9]]
3 7
[[2305843009213693952, 7], [2305843009213693952, 9], [2305843009213693952, 8]]
[[2305843009213693952, 8], [2305843009213693952, 9]]
0 1
[[2305843009213693952, 9]]
3 3
0 5 8 1 3 inf inf inf inf 10 
'''