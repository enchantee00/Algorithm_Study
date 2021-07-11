import sys



def least_diff(array):
    global ans_log
    if N % 2 == 0:
        for i in range(N // 2):
            ans_log.append(array[2*i])
        del array[0::2]
        array.reverse()
        for s in array:
            ans_log.append(s)
    else:
        for i in range(N // 2 + 1):
            ans_log.append(array[2*i])
        del array[0::2]
        array.reverse()
        for s in array:
            ans_log.append(s)
    
    return



T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    log = list(map(int, sys.stdin.readline().split()))
    sort_log = sorted(log)
    ans_log = []
    least_diff(sort_log)
    max_value = 0
    for i in range(len(ans_log)):
        check = abs(ans_log[i] - ans_log[i-1])
        if check > max_value:
            max_value = check
    print(max_value)