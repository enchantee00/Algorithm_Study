import sys
W, H= map(int, sys.stdin.readline().split())
N= int(sys.stdin.readline())
shops= []
for i in range(N):
    shops.append(list(map(int, sys.stdin.readline().split())))
dong= list(map(int, sys.stdin.readline().split()))
#shop, donggeun -> [0] == 동서남북 결정, [1] 기준점으로부터 떨어진 거리

def Compare(donggeun, shop):
    global count
    num= shop[1] + donggeun[1]
    if donggeun[0] == 1:
        if shop[0] == 2:
            if num > W:
                ans= 2*W - num
                count+= (ans + H)
            else:
                count+= (num + H)
        elif shop[0] == 3:
            count+= num
        else:
            count += (shop[1] + W - donggeun[1])

    elif donggeun[0] == 2:
        if shop[0] == 1:
            if num > W:
                ans= 2*W - num
                count += (ans + H)
            else:
                count += (num + H)
        elif shop[0] == 3:
            count+= (donggeun[1] + H - shop[1])
        else:
            count+= (H + W - num)
    
    elif donggeun[0] == 3:
        if shop[0] == 4:
            if num > H:
                ans= 2*H - num
                count+= (ans + W)
            else:
                count+= (num + W)
        elif shop[0] == 1:
            count+= num
        else:
            count+= (H - donggeun[1]+ shop[1])
    
    else:
        if shop[0] == 4:
            if num > H:
                ans= 2*H - num
                count+= (ans + W)
            else:
                count+= (num + W)
        elif shop[0] == 1:
            count+= (W - shop[1] + donggeun[1])
        else:
            count+= (H + W - num)



count= 0
for i in shops:
    if i[0] == dong[0]:
        count+= abs(i[1] - dong[1]) #절댓값의 차이 = 동근과 가게의 거리 차
    else:
        Compare(dong, i)

print(count)
