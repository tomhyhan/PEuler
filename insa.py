def solution(scores):
    
    scores.sort(key= lambda x: (-x[0], x[1]))
    print(scores)    
    
    new_scores = [scores[0]]
    minb = scores[0][1]
    for i in range(1, len(scores)):
        pass
    # won_f, won_s = scores[0]
    
    # for i in range(len(scores)):
    #     scores[i] = [sum(scores[i]), *scores[i]]

    # scores.sort(reverse=True)
    # print(scores)
    # for i, score in enumerate(scores):
    #     _, f, s = score
        
    #     if f == won_f and s == won_s:
    #         return i + 1
        
    #     if f > won_f and s > won_s:
    #         return -1
    
    # raise Exception()

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))