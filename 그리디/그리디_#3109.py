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
                    heapq.heappush(queue, [seq, nx, ny]) # 보통 이렇게 힙을 쓰진 않는다고 함

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

# Python3로는 시간초과, Pypy3로 통과
-----------------------------------------------------------------------------------
# <sol>

def solve(i, j): 
    if j == c-1: 
        return True 
    for d in dx: # DFS & 재귀 사용 - 정석풀이법
        if 0<=i+d<r and table[i+d][j+1] == '.' and not visit[i+d][j+1]: 
            visit[i+d][j+1] = True 
            if solve(i+d, j+1): 
                return True 
    return False

# 재귀 & DFS에 대한 공부 필요
# 아직 왜 내 코드가 Python3에서 시간초과가 나왔는지는 의문
