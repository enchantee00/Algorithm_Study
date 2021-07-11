import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
n = input().rstrip()
numbers, idx = [], -1
for i in n:
    idx += 1
    heapq.heappush(numbers, [int(i), idx])

for _ in range(K):
    heapq.heappop(numbers)

numbers = sorted(numbers, key = lambda x: x[1])
ans = ''
for i in numbers:
    ans += str(i[0])

print(int(ans))