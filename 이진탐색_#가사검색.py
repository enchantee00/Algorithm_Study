#프로그래머스

def solution(words, queries):
        
    global ans
    ans = [0] * len(queries)


    def wq_compare(q, w, num):
        if q[-1] == "?" and q[0] == "?":
            
            ans[num] += 1

            
        elif q[0] == "?":
            idx = -1
            while q[idx] != "?":
                if q[idx] == w[idx]:
                    idx -= 1
                else:
                    return
                
            ans[num] += 1

            
        else:
            idx = 0
            while q[idx] != "?":
                if q[idx] == w[idx]:
                    idx += 1
                else:
                    return
                
            ans[num] += 1
            
        return

    words_lst = []
    for i in words:
        words_lst.append((i, len(i)))

    queries_lst = []
    for i in queries:
        queries_lst.append((i, len(i)))

    num = -1
    for i in queries_lst:
        num += 1
        for s in words_lst:
            if i[1] == s[1]:
                wq_compare(i[0], s[0], num)
            else:
                pass

    return ans