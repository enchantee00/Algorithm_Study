import heapq
import sys


input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = {i : {} for i in range(1, V+1)}
for i in range(E):
    u, v, w = map(int, input().split())
    if v in graph[u].keys() and graph[u][v] <= w: 
        pass
    else:
        graph[u].update({v : w})

    
def function(graph, start):
    distances = {i : float('inf') for i in range(1, V+1)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for new_node, new_distance in graph[current_node].items():
            distance = current_distance + new_distance
            if distance < distances[new_node]:
                distances[new_node] = distance
                heapq.heappush(queue, [distance, new_node])


    for s in distances.values():
        if type(s) == int:
            print(s)
        else:
            print('INF')

    return

function(graph, start)