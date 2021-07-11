import sys
input = sys.stdin.readline

N, K = int(input().split())
lst, dp = [], []
for i in range(N):
    val = list(int(input().split()))
    lst.append(val)
    dp.append(0)
lst.sort()

for i in range(N-1, -1, -1):
    check = lst[i]
    rem 
    if lst[i][0] >= K//2:
        pass
    else:
        dp[i] = max()

