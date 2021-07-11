import sys
import heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = {i : [] for i in range(1, N + 1)}
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    
def Dijkstra(graph, start):
    distances = {i : float('inf') for i in range(1, N + 1)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        for new_node in graph[current_node]:
            distance = current_distance + 1
            if distance < distances[new_node]:
                distances[new_node] = distance
                heapq.heappush(queue, [distance, new_node])
    
    for i, s in distances.items():
        if s == K:
            heapq.heappush(queue, i)
        else:
            pass

    if len(queue) < 1:
        print(-1)
    else:
        for s in range(len(queue)):
            print(heapq.heappop(queue))

    return

Dijkstra(graph, X)
                

    