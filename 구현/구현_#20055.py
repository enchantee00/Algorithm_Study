import sys
N, K= map(int, sys.stdin.readline().split())
belt= list(map(int, sys.stdin.readline().split()))
robot= [0] * N

def conveyor(a):
    a.insert(0, a[-1])
    a.pop()

def conveyor_robot(b):
    b.insert(0, 0)
    b.pop()

def stage(belt, robot):
    stage_num= 1
    while True:

        conveyor(belt)          #조건 1
        if robot[N-1] == 1:
            robot[N-1] = 0
        conveyor_robot(robot)
        if robot[N-1] == 1:
            robot[N-1] = 0


        for i in range(N-2, -1, -1):        #조건 2
            if belt[i+1] > 0 and robot[i] == 1 and robot[i+1] != 1: 
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1
            


        if belt[0] > 0:         #조건 3
            robot[0] = 1
            belt[0] -= 1
        if belt.count(0) >= K:
            break

        stage_num += 1

    return stage_num

print(stage(belt, robot))

