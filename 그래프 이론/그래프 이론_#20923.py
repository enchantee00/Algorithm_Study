from collections import deque
import sys
N, M= map(int, sys.stdin.readline().split())
queue_d = deque()
queue_s = deque()
deck_d= deque()
deck_s= deque()
for i in range(N):
    d, s= map(int, sys.stdin.readline().split())
    queue_d.append(d)
    queue_s.append(s)


def dodo_ring():
    global trial
    deck_d.reverse()
    deck_s.reverse()
    for i in deck_d:
        queue_d.appendleft(i)
    for i in deck_s:
        queue_d.appendleft(i)

    trial+= 1
    return


def suyeon_ring():
    global trial
    deck_d.reverse()
    deck_s.reverse()
    for i in deck_d:
        queue_s.appendleft(i)
    for i in deck_s:
        queue_s.appendleft(i)

    trial+= 1
    return



trial= 0
while trial < M:
    card_d= queue_d.pop()
    card_s= queue_s.pop()

    deck_d.append(card_d)
    if card_d or deck_s[-1] == 5:   #도도가 종 침
        dodo_ring()
    deck_s.append(card_s)
    if deck_d[-1] + card_s == 5:    #수연이가 종 침
        suyeon_ring()
    
    
    if len(queue_s) == 0:
        print('do')
        sys.exit()
    elif len(queue_d) == 0:
        print('su')
        sys.exit()
    else:
        pass

if queue_d > queue_s:
    print('do')
elif queue_s > queue_d:
    print('su')
else:
    print('dosu')
    

    