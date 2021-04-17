from statistics import multimode
import sys
N= int(sys.stdin.readline())
lst= []
for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort()
freq= multimode(lst)

average= round(sum(lst) / len(lst))
mid= lst[len(lst) // 2]
frequent= freq[1] if len(freq) > 1 else freq[0]
ran= lst[-1] - lst[0]


print("%g"%(average))
print(mid)
print(frequent)
print(ran)

-----------------------------------------------------------
#시간초과

import sys
N= int(sys.stdin.readline())
lst= []
for i in range(N):
    lst.append(int(sys.stdin.readline()))



def frequency_dic(a):
    frequency= [0] * len(set(a))
    checked_lst= []

    s= 0
    for i in range(len(a)):
        if a[i] not in checked_lst:
            checked_lst.append(a[i])
            frequency[s] += 1
            s+= 1
        else:
            frequency[-1] += 1

    maxi= max(frequency)
    if frequency.count(maxi) > 1:
        adcd= [num for idx, num in enumerate(checked_lst) if frequency[idx] == maxi]
        return adcd[1]
    else:
        return checked_lst[frequency.index(maxi)]

        
        
lst.sort()
average= round(sum(lst) / len(lst))
mid= lst[len(lst) // 2]
frequent= frequency_dic(lst)
ran= lst[-1] - lst[0]



print("%g"%(average))
print(mid)
print(frequent)
print(ran)
