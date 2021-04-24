from collections import deque
import sys

N, M, V= map(int, sys.stdin.readline().split())
string_lst= []
num_lst= []
for i in range(M):
    a= tuple(map(int, sys.stdin.readline().split()))
    string_lst.append(a)
    num_lst.extend(a)

num_lst= list(set(num_lst))

graph= [[] for _ in range(N+1)]
for i in range(1, N+1):
    for s in string_lst:
        if i in s:
            node_idx= s.index(i)
            graph[i].append(s[node_idx - 1])
    graph[i].sort()

def DFS(chart, v, visited):
    visited[v] = True
    print(v, end= ' ')

    for i in chart[v]:
        if not visited[i]:
            DFS(chart, i, visited)




def BFS(chart, start, visited):
    queue= deque([start])
    visited[start]= True
    while queue:
        v= queue.popleft()
        print(v, end= ' ')
        for i in chart[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True




visited_DFS= [False] * (N+1)
visited_BFS= [False] * (N+1)

DFS(graph, V, visited_DFS)
print()
BFS(graph, V, visited_BFS)