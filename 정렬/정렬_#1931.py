import sys
N = int(sys.stdin.readline())
schedule = []
room = []
for i in range(N):
    schedule.append(list(map(int, sys.stdin.readline().split())))

schedule = sorted(schedule, key = lambda x : (x[1], x[0]))  #(끝나는 시간 -> 시작하는 시간) 기준으로 정렬

room.append(schedule[0][1])
room_num = 1
for i in range(1, N):
    if room[0] <= schedule[i][0]:
        room.pop()
        room.append(schedule[i][1])
        room_num += 1
    else:
        pass

print(room_num)

