def solution(n, lost, reserve):
    lost = set(map(int, lost))
    reserve = set(map(int, reserve))
    reserve -= lost
    for l in lost:
        if (l - 1) in reserve:
            reserve.remove(l - 1)
            continue            

        if (l + 1) in reserve:
            reserve.remove(l+1)
            continue
        n -= 1
    # print(n)
    return n

def solution(n, lost, reserve):
    lost = set(map(int, lost))
    reserve = set(map(int, reserve))
    areserve = reserve - lost
    alost = lost - reserve
    for r in areserve:
        if (r - 1) in alost:
            alost.remove(r - 1)
            continue            

        if (r + 1) in alost:
            alost.remove(r+1)
            continue

    # print(n- len(lost))
    return n-len(lost)

solution(5, [2, 4], [1, 3, 5])
solution(3, [3], [1])