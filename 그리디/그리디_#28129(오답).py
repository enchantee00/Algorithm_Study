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

# 아이디어조차 틀려먹은 코드
-------------------------------------------------------------
# <sol>

import sys

N,K = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().strip()))

result = []
delNum = K

for i in range(N):
    while delNum>0 and result:
        if result[-1] < nums[i]: 
            result.pop()
            delNum-=1
        else:
            break
    result.append(nums[i])
    
for i in range(N-K):
    print(result[i],end="")
    
# 스택 사용 -> (Last in First out 구조)
