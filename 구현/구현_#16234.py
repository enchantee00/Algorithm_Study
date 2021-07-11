import sys
N, L, R= map(int, sys.stdin.readline().split())
continent= []
for i in range(N):
    continent.append(list(map(int, sys.stdin.readline().split())))

def CheckDiff(a):
    allies_position= [[(0,0)]] #동맹 국가들 위치 받기 (동맹국들끼리 []로 묶어주기)
    allies_population= [[a[0][0]]] #동맹 국가들 인구수 받기 (동맹국들끼리 []로 묶어주기)
    for i in range(len(a)):
        for s in range(len(i)):
            try:
                if L <= abs(a[i][s] - a[i][s+1]) <= R:
                    allies_population.append(a[i][s+1])
                    allies_position.append((i, s+1))
            except IndexError:
                pass
            try:
                if L <= abs(a[i][s] - a[i+1][s]) <= R:
                    allies_population.append(a[i+1][s])
                    allies_position.append((i+1, s))
            except IndexError:
                pass
            else:
                allies_position.append([(i, s)])
                allies_population.append([a[i][s]])


