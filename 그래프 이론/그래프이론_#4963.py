from collections import deque
import sys

move= [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def BFS(h, w):
    queue= deque([(h, w)])
    island= [[h, w]]

    visited[h][w]= True

    while queue:

        h, w = queue.popleft()

        for i in move:

            nh= h + i[0]
            nw= w + i[1]

            if nh in range(H) and nw in range(W):
                if graph[nh][nw] == 1 and visited[nh][nw] == False:
                    visited[nh][nw] = True
                    queue.append((nh, nw))
                    island.append([nh, nw])

    return island



while True:
    W, H= map(int, sys.stdin.readline().split())
    if W == 0 and H == 0:
        break
    graph= []
    for i in range(H):
        a= list(map(int, sys.stdin.readline().split()))
        graph.append(a)

    visited= [[False] * W for _ in range(H)]

    count= 0
    for i in range(H):
        for s in range(W):
            if not visited[i][s] and graph[i][s] == 1:
                island_count = BFS(i, s)
                if len(island_count) > 0:
                    count += 1
    
    print(count)