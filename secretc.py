from itertools import combinations 
    
def solution(n, q, ans):
    n_secrets = 0
    for combo in combinations(range(1, n+1), 5):
        valid = True
        combo = set(combo)
        for question, answer in zip(q, ans):
            if len(combo & set(question)) != answer:
                valid = False
                break
            
        if valid:
            n_secrets += 1
    return n_secrets
    print(n_secrets)
    

solution(10, 
         [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], 
         [2, 3, 4, 3, 3])

# [1, 2, 3, 5, 8]
# [1, 3, 5, 8, 12]
# [2, 4, 5, 8, 12]
# [2, 5, 8, 9, 10]
# [5, 8, 9, 10, 12]
solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1])

