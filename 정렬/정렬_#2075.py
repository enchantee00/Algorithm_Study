import heapq
import sys
N = int(sys.stdin.readline())
graph = []
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for s in lst:
        heapq.heappush(graph, s)
        if len(graph) > N:
            heapq.heappop(graph)

ans = heapq.heappop(graph)
print(ans)