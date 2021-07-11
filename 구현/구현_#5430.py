import sys
from itertools import groupby


def func(array_chunk, array):
    R_num= 0
    for i in array_chunk:
        if 'R' in i:
            R_num += len(i)     #매번 뒤집지 않아도 된다. -> 시간 복잡도 O(N)
        else:
            if len(array) >= len(i):
                cut= len(i)
                if R_num % 2 == 0:
                    del array[0:cut]
                else:
                    del array[len(array) - cut:]
            else:
                print('error')
                return

    if R_num % 2 == 0:
        ans= ''.join(str(array).split())     #리스트 출력할 때, 공백 없이 하기 위해서 string으로 바꿔준다.
        print(ans)
    else:
        array.reverse()
        ans= ''.join(str(array).split())
        print(ans)


T= int(sys.stdin.readline())
for i in range(T):
    p= sys.stdin.readline().strip('\n')     #항상 sys.stdin.readline()에는 '\n'이 뒤에 붙는다.
    n= int(sys.stdin.readline())
    s= sys.stdin.readline().strip('\n')
    if len(s) == 2:
        array= []
    else:
        array= list(map(int, s.strip('[]\n').split(',')))
    array_chunk= [''.join(g) for _, g in groupby(p)]

    func(array_chunk, array)