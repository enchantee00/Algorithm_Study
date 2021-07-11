import sys
import heapq

input = sys.stdin.readline
R, C = map(int, input().split())
graph = []
visited = [[0] * C for _ in range(R)]
for _ in range(R):
    graph.append(input().rstrip())

dx = [1]
dy = [-1, 0 ,1]
queue = []

ans = 0
for i in range(R):
    a = True
    x, y = 0, i
    seq = C
    if graph[y][x] == '.':
        visited[y][x] = 1 
        while x < C - 1:
            seq -= 1
            for s in range(3):
                nx, ny = x + dx[0], y + dy[s]
                if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] == '.' and visited[ny][nx] == 0:
                    heapq.heappush(queue, [seq, nx, ny])

            if queue:
                null, x, y = heapq.heappop(queue)
                visited[y][x] = 1
            else:
                a = False
                queue = []
                break
                
        if a:
            ans += 1
            queue = []

    else:
        pass

print(ans)