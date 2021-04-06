city_num= int(input())
street_len= list(map(int, input().split()))
oil_price= list(map(int, input().split()))

count= 0
money= 0
s= 0
for i in range(len(oil_price)-1):
    count += street_len[i]
    if i == len(oil_price) - 2:
        money += oil_price[s] * count
        break
    else:
        if oil_price[s] > oil_price[i+1]:
            money += oil_price[s] * count
            count= 0
            s = i + 1
print(money)


