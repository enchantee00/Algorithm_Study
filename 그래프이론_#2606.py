from collections import deque
import sys
N= int(sys.stdin.readline())
pairs= int(sys.stdin.readline())
lst= []
for i in range(pairs):
    lst.append(tuple(map(int, sys.stdin.readline().split())))

graph= [[] for _ in range(N+1)]
for i in range(1, N+1):
    for s in lst:
        if i in s:
            graph[i].append(s[s.index(i) - 1])

visited= [False] * (N+1)
count= 0

def BFS(chart, start, visited):
    global count
    queue= deque([start])
    visited[start]= True
    while queue:
        v= queue.popleft()
        count+= 1
        for i in chart[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

BFS(graph, 1, visited)
print(count - 1)
            
