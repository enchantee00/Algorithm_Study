#2차원 배열 만들기
a,b = map(int, input().split())
chart_A= []
chart_B= []
chart= []
for i in range(a):
    chart_A.append(list(map(int, input())))

for i in range(a):
    chart_B.append(list(map(int, input())))

for i in range(a):
    ans= [s - t for s, t in zip(chart_A[i], chart_B[i])]
    chart.append(ans)

#바꾸기 함수
def Tipping(k, row, column):
    for i in range(row, row+3):
        for s in range(column, column+3):
            if k[i][s] == 0:
                k[i][s]= 1
            else:
                k[i][s]= 0

count= 0
for i in range(a-2):
    for s in range(b-2):
        if chart[i][s] == 0:
            pass
        else:
            Tipping(chart, i, s)
            count+= 1

for i in range(a):
    if 1 in chart[i] or -1 in chart[i]:
        count= -1

print(count)