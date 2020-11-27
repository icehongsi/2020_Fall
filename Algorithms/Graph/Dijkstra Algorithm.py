import time
class dijkstra_class:
    def __init__(self):
        n, e = int(input()), int(input())
        self.distance, self.edge, self.locator, self.heap = {}, {}, [None] * n, []
        '''
        edge) key: 시작 엣지, value: (끝 엣지, 가중치)
        distance) key: 그래프상에서의 노드 번호, value: initial node에서 현 노드까지의 거리
        locator) i번쨰 인덱스에는 힙에서의 위치가 저장되어 있음  
        heap) 최소값을 쉽게 꺼내기 위한 자료구조, 0번째 인덱스는 현재 그래프 노드 내 가장 작은 거릿값을 가지고 있는 노드 번호를 가리킴
        '''

        for i in range(e):
            temp = list(map(int, input().split())) #시작 노드, 끝 노드, 둘을 잇는 엣지의 가중치
            if temp[0] in self.edge:
                self.edge[temp[0]].append([temp[1], temp[2]])

            else:
                self.edge[temp[0]] = [temp[1], temp[2]]  # edge 딕셔너리에 시작 노드를 key로, 시작 노드와 이어져있는 다른 노드의 리스트와 그 가중치를 nested list 형태로 저장
                self.distance[temp[0]] = 1 << 61
                self.heap.append(temp[0])
                self.locator[temp[0]] = len(self.heap) - 1
                self.heapifyUp()

        self.distance[0] = 0
        self.heapifyUp()
        self.dijkstra()


    def retrieveMax(self):
        if len(self.heap) == 0:
            return
        n = len(self.heap) - 1
        self.heap[0], self.heap[n] = self.heap[n], self.heap[0]
        self.locator[n] = 0
        result = self.heap.pop()
        self.locator[result] = None
        self.heapifyDown()
        return result

    def heapifyDown(self, n = 0):
        while True:
            L, R, M = 2 * n + 1, 2 * n + 2, n
            if L >= len(self.heap):
                break
            if self.distance[self.heap[L]] < self.distance[self.heap[M]]:
                M = L
            if R < len(self.heap) and self.distance[self.heap[R]] < self.distance[M]:
                M = R
            if n == M:
                break
            else:
                self.heap[n], self.heap[M] = self.heap[M], self.heap[n]
                self.locator[M] = n
                self.locator[n] = M
                n = M



    def heapifyUp(self, n = -1):
        if n == -1: #기본값: heap의 마지막 원소를 기준으로 heapifyUp 실행
            n = len(self.heap) - 1
        while n > 0:
            target = (n - 1) // 2 #이는 heap의 인덱스
            print(target)
            print(self.distance)
            print(self.locator)
            print(self.heap)
            print(target, n)
            if self.distance[self.heap[target]] > self.distance[self.heap[n]]: # distance를 비교해서, 자식 노드의 distance가 더 작을 경우 위로 올려보냄
                self.locator[target] = n
                self.locator[n] = target
                self.heap[target], self.heap[n] = self.heap[n], self.target[target]
            else:
                break

    def dijkstra(self):
        while self.heap:
            target = self.retrieveMax()
            print("dijkstra", target)
            for i in self.edge[target]: #i[0]: terminal node, i[1]: weight
                    if self.distance[i[0]] > self.distance[target] + i[1]:
                        self.distance[i[0]] = self.distance[target] + i[1]
                        self.heapifyUp(self.node[self.visited[i[0]]])

solution = dijkstra_class()