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
    frequency= [0] * len(set(a))    #[0,0,0] & [2,3,4] -> frequency, checked_lst에 있는 원소들 모두 같은 인덱스에 배열(서로 상응)
    checked_lst= []

    s= 0 
    for i in range(len(a)):
        if a[i] not in checked_lst:
            checked_lst.append(a[i])
            frequency[s] += 1   #새로운 원소 들어올 때만 하나씩 올려준다
            s+= 1   #s값 하나 올려주고 새로운 원소 들어올 때까지 대기
        else:   
            frequency[-1] += 1   #중복되는 원소, a[i]가 나왔을 떄 이미 lst.sort() 했기 때문에 [-1] 가능

    maxi= max(frequency)
    if frequency.count(maxi) > 1:
        adcd= [num for idx, num in enumerate(checked_lst) if frequency[idx] == maxi]   #frequency[idx] 최대일 떄의 cheked_lst[idx]의 값들의 집합
        return adcd[1]  #lst.sort()에 의해 [1]이 2번째로 작은 값
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
