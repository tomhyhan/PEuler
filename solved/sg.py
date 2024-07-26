def solution(sticker):
    if len(sticker) == 1:
        return sticker[-1]
    
    if len(sticker) == 2:
        return max(sticker[-1], sticker[-2])
    
    DP1 = [0] * len(sticker)
    
    DP1[0] = sticker[0]
    DP1[1] = max(sticker[0], sticker[1])
    
    for i in range(2, len(sticker) - 1):
        DP1[i] =  max(DP1[i-1], sticker[i] + DP1[i-2])
    
    DP2 = [0] * len(sticker)
    
    DP2[1] = sticker[1]
    DP2[2] = max(sticker[1], sticker[2])
    
    for i in range(3, len(sticker) ):
        DP2[i] =  max(DP2[i-1], sticker[i] + DP2[i-2])
    
    # print(DP1)
    # print(DP2)
    
    return max(DP1[-2], DP2[-1])

solution([14, 6, 5, 11, 3, 9, 2, 10])
solution([1, 3, 2, 5, 4])