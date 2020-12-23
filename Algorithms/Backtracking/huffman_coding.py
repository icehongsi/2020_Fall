import heapq

coding_list = list(map(int, input().split()))
coding_hash = dict(zip(coding_list,range(len(coding_list))))
heap = []
for i, val in enumerate(coding_list):
    heapq.heappush(heap, (val, i))

while len(heap) > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    print(a, b)
    heapq.heappush(heap,
                   (a[0] + b[0], str(a[1]) + " " + str(b[1]))
                   )

print(heap[0])

