import sys
N = int(sys.stdin.readline())
locals = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())

sort_local = sorted(locals)
average = budget // N
rem = budget % N
previous_avg_index = 0


def binary_search (array, avg, left, right, rem):
    global ans
    global previous_avg_index
    while (right - left) > 1:
        mid = (right + left) // 2
        if array[mid] > avg:
            right = mid
        elif array[mid] < avg:
            left = mid
        else:
            avg_index = mid
            break
    else:
        avg_index = left

    remainder = avg * (avg_index - previous_avg_index + 1) - sum(array[previous_avg_index:avg_index + 1]) + rem
    try:
        a = divmod(remainder, (len(array) - (1 + avg_index)))
    except ZeroDivisionError:
        return array[-1]

    avg += a[0]
    rem = a[1]

    if avg > array[avg_index + 1]:
        previous_avg_index = avg_index + 1
        return binary_search(array, avg, avg_index + 1, len(array) - 1, rem)
    else:
        return avg


ans = binary_search(sort_local, average, 0, len(sort_local) - 1, rem)
print(ans)

##################################################################################

#<solution>

import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
m = int(input())
low, high = 0, max(s)
while low <= high:
    mid = (low + high) // 2
    num = 0
    for i in s:
        if i >= mid: num += mid
        else: num += i
    if num <= m: low = mid + 1
    else: high = mid - 1
print(high)