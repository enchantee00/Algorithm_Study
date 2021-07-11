import sys
input = sys.stdin.readline

N = int(input())

def func(N):
    count = 0
    for i in range(10 ** (N-1), 10 ** N):
        i = str(i)
        j = 1
        while j < N:
            num = int(i[j-1])
            if int(i[j]) == num + 1 or num - 1:
                j += 1
            else:
                continue

        count += 1

    return count

print(func(N))

