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
