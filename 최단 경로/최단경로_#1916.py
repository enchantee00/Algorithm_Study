import sys
import heapq

input = sys.stdin.readline
N = int(input())
M = int(input())

graph = {i : {} for i in range(1, N+1)}
for i in range(M):
    a, b, c = map(int, input().split())
    if b in graph[a].keys() and graph[a][b] <= c:
        pass
    else:
        graph[a].update({b : c})

start, destination = map(int, input().split())


def Dijsktra(graph, start):
    fare_graph = {i : float('inf') for i in range(1, N+1)}
    fare_graph[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        current_fare, current_city = heapq.heappop(queue)
        if fare_graph[current_city] < current_fare:
            continue

        for next_city, next_fare in graph[current_city].items():
            fare = current_fare + next_fare
            if fare < fare_graph[next_city]:
                fare_graph[next_city] = fare
                heapq.heappush(queue, [fare, next_city])
            
    return fare_graph[destination]


print(Dijsktra(graph, start))