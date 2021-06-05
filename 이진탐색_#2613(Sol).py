import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Beads = list(map(int, input().split()))

######################################################

#<solution>

from sys import stdin

def intJoin(arr): return " ".join([str(i) for i in arr])

def reGroupping(gca):
  global m
  lackCount = m - len(gca)
  additionalArr = []
  for i in range(len(gca)-1, -1, -1):
    while(gca[i] != 1):
      gca[i] = gca[i]-1
      additionalArr.append(1)
      if len(additionalArr) == lackCount:
        return gca+additionalArr
    
def groupCount(mid):
  global arr
  gc, _sum, i = (0, 0, 0) # gc = groupCount
  while(i < len(arr)):
    _sum += arr[i]
    if mid == _sum:
      gc += 1
      _sum = 0
    elif mid < _sum:
      if _sum != arr[i]: i -= 1
      gc += 1
      _sum = 0
    i += 1
  if _sum < mid and _sum != 0: gc += 1
  return gc

def getGroupCountArr(ms):
  global arr
  gca, count, _sum, i = ([], 0, 0, 0) # gc = groupCount
  while(i < len(arr)):
    _sum += arr[i]
    count += 1
    if ms == _sum:
      gca.append(count)
      _sum = 0
      count = 0
    elif ms < _sum:
      if count == 1: gca.append(1)
      else:
        gca.append(count-1)
        i -= 1
      count, _sum = (0, 0)
    i += 1
  if _sum < ms and count != 0: gca.append(count)
  return gca
  
        
def answer():
  global n, m, arr
  start, end, ms, gc = (max(arr), sum(arr), 0, 0) # ms = maxSum
  while(start <= end):
    mid = (start+end)//2
    gc = groupCount(mid)
    if gc <= m: ms, end = (mid, mid-1)
    else: start = mid+1
  print(ms)
  
  gca = getGroupCountArr(ms)
  if len(gca) != m: gca = reGroupping(gca)
  print(intJoin(gca))
  
  
n, m = map(int, input().split())
arr = list(map(int, stdin.readline().split()))
answer()