import sys
N, M= sys.stdin.readline().split()
maze= []
for i in range(N):
    a= sys.stdin.readline()
    lst= []
    for s in range(len(a) - 1):
        lst.append(a[s])
    maze.append(lst)

pos= [0, 0]

dx= [1, 0] ## 오른쪽, 위쪽만 구성
dy= [0, 1]


count= 0
while pos[0] != N or pos[1] != M:
    right_nx= pos[0] + dx[0]
    right_ny= pos[1] + dy[0]
    down_nx= pos[0] + dx[1]
    down_ny= pos[1] + dy[1]
    if maze[down_ny][down_nx] == 1:
        pos[0] = down_nx
        pos[1] = down_ny
        count+= 1
    else:
        pos[0] = right_nx
        pos[1] = right_ny
        count+= 1

print(count)