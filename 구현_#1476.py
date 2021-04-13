import sys
E,S,M= map(int, sys.stdin.readline().split())

start= [1,1,1]
count= 1
while start[0] != E or start[1] != S or start[2] != M:
    start[0] += 1
    start[1] += 1
    start[2] += 1
    if start[0] > 15:
        start[0]= 1
    if start[1] > 28:
        start[1]= 1
    if start[2] > 19:
        start[2]= 1
    count += 1

print(count)