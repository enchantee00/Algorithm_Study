n = int(input())
strength = []
dp = []
for i in range(n):
    a = int(input())
    strength.append(a)
    dp.append(a)
dp.append(0)
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])