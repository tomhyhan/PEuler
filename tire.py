from itertools import permutations

def solution(k, dungeons):
    n_d = len(dungeons)
    max_cnt = 0
    for perms in permutations(range(n_d), n_d):
        cnt = 0
        ck = k 
        for perm in perms:
            req_k,sk = dungeons[perm]
            if ck >= req_k:
                ck -= sk
                cnt +=1
            else:
                break
            
        max_cnt = max(max_cnt, cnt)
    return max_cnt
# 3
solution(80, [[80,20],[50,40],[30,10]])