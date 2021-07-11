import sys
from types import GetSetDescriptorType
N, C= map(int, sys.stdin.readline().split())
M= int(sys.stdin.readline())
box_info= []
for i in range(M):
    s= list(map(int, sys.stdin.readline().split()))
    box_info.append(s)

box_info= sorted(box_info, key= lambda x: (x[0], x[1]))
box_info_dic= {}    #보내는 마을 기준 딕셔너리로 박스 분류
for k in box_info:
    if k[0] in box_info_dic.keys():
        box_info_dic[k[0]].append(k)
    else:
        box_info_dic.update({k[0]: [k]})

def on(village_num, tr):
    global truck_load
    global truck
    while True:
        for i in tr[village_num]:
            dest= i[1]          #목적지
            dest_load= i[2]     #목적지 배달량

            if truck_load + dest_load > C:
                if dest in truck.keys():
                    truck[dest] += (C - truck_load)
                    truck_load = C
                else:
                    truck.update({dest: (C - truck_load)})
                    truck_load = C
            else:
                truck_load += dest_load
                if dest in truck.keys():
                    truck[dest] += dest_load
                else:
                    truck.update({dest: dest_load})

            if truck_load >= C:
                continue

        break

    return



truck= {}               #도착지 기준 딕셔너리로 박스 정보 분류
truck_load= 0           #트럭의 용량
delivered_packages= 0   #배달한 박스 수



on(1, box_info_dic)                 #첫 번째 마을엔 내릴 박스 없으니, 먼저 상차 실행
for t in range(2, N+1):             #두 번째 마을부터
    if truck[t] > 0:                #방문한 마을에 하차할 박스 있는지 확인
        truck_load -= truck[t]      #하차 먼저
        delivered_packages += truck[t]
        del truck[t]
        if t == N:
            break
        if t in box_info_dic.keys():
            on(t, box_info_dic)
    else:
        if t in box_info_dic.keys():
            on(t, box_info_dic)

print(delivered_packages)
