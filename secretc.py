from itertools import combinations 

def pass_rule(idx, questions, answers, secret):
    for i in range(idx+1):
        if len(secret & set(questions[i])) != answers[i]:
            return False  
    return True
    
def solution(n, q, ans):

    stack = [(0, set())]
    
    n_secrets = set()
    while stack:
        idx, secret = stack.pop()

        if idx == len(q): 
            if len(secret) == 5:
                n_secrets.add(tuple(secret)) 
            continue
        
        for comb in combinations(q[idx], ans[idx]):
            comb = set(comb)
            new_secret = secret | comb
            
            if len(new_secret) > 5:
                continue
            # print(new_secret, set(q[idx]), ans[idx])
            print(new_secret & set(q[idx]))
            # print()
            if pass_rule(idx, q, ans, new_secret):
                stack.append((idx+1, new_secret))

    print(n_secrets)
    
# solution(10, 
#          [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], 
#          [2, 3, 4, 3, 3])

# 3, 8, 9, 10, 12
solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1])

