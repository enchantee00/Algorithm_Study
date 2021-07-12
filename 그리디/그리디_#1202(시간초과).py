import sys
import heapq


def binary_search(array, target, start, end): # 이진탐색 알고리즘
    if start > end:
        return None
    if end - start <= 1:
        return end

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid)
    elif array[mid] < target:
        return binary_search(array, target, mid, end)


input = sys.stdin.readline
N, K = map(int, input().split())
gems, bags = [], []
for _ in range(N):
    a, b = map(int, input().split())
    heapq.heappush(gems, [-b, a])
for _ in range(K):
    bags.append(int(input()))


bags.sort() # 파이썬 sort() 내장함수 정렬 알고리즘 사용 -> 굳이 정렬에 알고리즘 사용할 필요 없음.
ans = 0
for _ in range(N):
    price, weight = heapq.heappop(gems)
    real_price = -price
    if len(bags) > 0:
        if weight <= bags[-1]:
            idx = binary_search(bags, weight, 0, len(bags) - 1) # 최악의 경우, 모든 보석에 대해서 이진 탐색을 해줘야 함 -> (시간 초과)
            del bags[idx] # del 쓰면서 리스트를 돌리는 것 -> 좋지 않은 방법
            ans += real_price
    else:
        break

print(ans)

# 기준을 가장 비싼 보석으로 잡기 실패 -> 기준 바꿔서 생각해보기
------------------------------------------------------------------------------------------

#<sol>
profitSum=0
canSteal=[]
while bags:
    bag=heapq.heappop(bags) # 힙을 사용하니까 굳이 del(시간 복잡도 O(N)) 사용 안해도 됨
    while items and items[0][0]<=bag:
        p=heapq.heappop(items)[1]
        heapq.heappush(canSteal,-p) # 최대 힙
    if canSteal:
        profitSum-=heapq.heappop(canSteal)
    elif not items: break
