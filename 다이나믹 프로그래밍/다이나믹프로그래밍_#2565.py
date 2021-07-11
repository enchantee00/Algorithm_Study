import sys
input = sys.stdin.readline

N = int(input())
lst = []
dp = [1] * N
for i in range(N):
    lst.append(list(map(int, input().split())))
lst.sort(key = lambda x : x[0])

for i in range(1, N):   #가장 긴 증가하는 부분 수열(LIS)
    for j in range(i):
        if lst[i][1] > lst[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
        else:
            pass

ans = N - max(dp)
print(ans)