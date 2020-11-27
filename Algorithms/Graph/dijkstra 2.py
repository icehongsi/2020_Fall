class dijkstra:
    def __init__(self):
        n = int(input())  # number of nodes
        e = int(input())  # number of edges
        self.edge = {0: []} #key: node number, value: edges (terminal / weight)
        self.distance = {0: 0} #key: node number, value: distance
        self.node = [0]
        for i in range(e):
            print(i)
            temp = list(map(int, input().split()))
            if temp[0] in self.edge:
                self.edge[temp[0]].append((temp[1], temp[2]))
            else: #temp[0] not in self.info
                self.edge[temp[0]] = [(temp[1], temp[2])]
                self.distance[temp[0]] = 1<<63
                self.node.append(temp[0])
                self.heapifyUp()
        print("init end")
        self.isvisited = [False] * (n-1)
        self.dijkstra()

    def heapifyUp(self, n = -1):
        if n == -1:
            n = len(self.node) - 1
        while n > 0:
            target = (n - 1) // 2
            if self.distance[self.node[target]] > self.distance[self.node[n]]:
                #swap
                self.node[target], self.node[n] = self.node[n], self.node[target]
                n = target
            else:
                break

    def heapifyDown(self, n = 0):
        while True:
            L, R, M = 2 * n + 1, 2 * n + 2, n
            if L >= len(self.node):
                break
            if self.distance[self.node[L]] < self.distance[self.node[M]]:
                M = L
            if R < len(self.node) and self.distance[self.node[R]] < self.distance[M]:
                M = R
            if n == M:
                break
            else:
                self.node[n], self.node[M] = self.node[M], self.node[n]
                n = M

    def dijkstra(self):
        print("dijkstra")
        while self.node:
            self.node[0], self.node[-1] = self.node[-1], self.node[0]
            target = self.node.pop()
            print('target', target)
            print(self.node)
            print(self.edge)
            print(self.distance)
            self.heapifyUp()
            if self.isvisited[target]:
                pass
            else:
                self.isvisited[target] = True
                print(self.isvisited)
                for i in self.edge[target]: #i[0]: terminal node, i[1]: weight
                    if self.distance[i[0]] > self.distance[target] + i[1]:
                        self.distance[i[0]] = self.distance[target] + i[1]
                        self.heapifyUp(i[0])


solution = dijkstra_class()