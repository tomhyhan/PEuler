def solution(scores):
    
    won_f, won_s = scores[0]
    scores.sort(key= lambda x: (-x[0], x[1]))
    
    rank = 0 
    maxb = float("-inf")
    for i in range(len(scores)):
        a, b = scores[i]
        
        if won_f < a and won_s < b:
            return -1
        
        if b >= maxb:
            maxb = b
            if a + b > won_f + won_s:
                rank += 1
    
    return rank + 1

    

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))