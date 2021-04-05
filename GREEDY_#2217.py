a= int(input())
lst= []
for i in range(a):
    c= int(input())
    lst.append(c)

lst.sort()
weight= [len(lst)*lst[0]]
for s in range(1, a):
    if lst[s] != lst[s-1]:
        weight_ele= (len(lst)-s)*lst[s]
        weight.append(weight_ele)
    else:
        weight.append(weight_ele)

print(max(weight))
