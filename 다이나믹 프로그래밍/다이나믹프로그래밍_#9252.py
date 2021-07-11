import sys
input = sys.stdin.readline

one = input()
two = input()

for i in range(len(one)):
    for j in range(i):
        if one[i]