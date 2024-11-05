import copy 

def solution(clockHands):
    n_rows = len(clockHands)
    n_cols = len(clockHands[0])

    min_flips = float('inf')
    for bits in range(4**n_rows):
        clockHands_tmp = copy.deepcopy(clockHands)

        flips=0
        for row in range(n_cols):
            if (req_flips := ((bits >> (row * 2)) & 3)):
                for dir in [(0,0),(0,1),(0,-1),(1,0),(-1,0)]:
                    fi = 0 + dir[0]
                    fj = row + dir[1]
                    if 0 <= fi < n_rows and 0 <= fj < n_cols:
                        clockHands_tmp[fi][fj] = (clockHands_tmp[fi][fj] + req_flips) % 4
                flips += req_flips
                        
        for i in range(n_rows-1):
            for j in range(n_cols):
                if clockHands_tmp[i][j] == 0:
                    continue
                flips_req = 4-clockHands_tmp[i][j]
                for dir in [(0,0),(0,1),(0,-1),(1,0),(-1,0)]:
                    ni = i + dir[0] + 1
                    nj = j + dir[1]
                    if 0 <= ni < n_rows and 0 <= nj < n_cols:
                        clockHands_tmp[ni][nj] = (clockHands_tmp[ni][nj] + flips_req) % 4
                flips += flips_req
        if sum(clockHands_tmp[-1]) == 0:
            min_flips = min(min_flips, flips)
                    
    return min_flips

from copy import deepcopy

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

def rotate(x, y, lst, rt) :
    length = len(lst)
    for k in range(5) :
        ax, ay = x + dx[k], y + dy[k]
        if -1 < ax < length and -1 < ay < length :
            lst[ay][ax] = ( lst[ay][ax] + rt ) % 4

def solution(clockHands):
    answer = float('inf')
    length = len(clockHands)
    
    for i in range(4 ** length) :
        tmp = 0
        tmp_clock = deepcopy(clockHands)
        for j in range(length) :
            rt = i % 4 ** ( j + 1 ) // 4 ** j
            if rt == 0 :
                continue
                
            rotate(j, 0, tmp_clock, rt)
            tmp += rt
        
        for y in range(1, length) :
            for x in range(length) :
                if tmp_clock[y-1][x] == 0 :
                    continue
                rt = 4 - tmp_clock[y-1][x]
                rotate(x, y, tmp_clock, rt)
                tmp += rt
        if sum(tmp_clock[-1]) == 0 : 
            answer = min(answer, tmp)
        for p in tmp_clock:
            print(p)
        print()
        if i == 10:
            break
                    
    return answer
                               
solution([[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]])