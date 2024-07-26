from collections import defaultdict, deque

def coutains_all_gems(unique_gems, gem_cnts):
    for gem in unique_gems:
        if gem_cnts[gem] == 0:
            return False
    return True

def solution(gems):
    n_unique = len(set(gems))
    answer_list = set()
    
    gem_cnts = defaultdict(int)
    bought = deque([])
    best = [1, len(gems)]
    for i, gem in enumerate(gems):
        gem_cnts[gem] += 1
        answer_list.add(gem)
        if len(bought) > 0 and gem == bought[0][0]:
            duplicate_gem = gem
            while gem_cnts[duplicate_gem] > 1:
                bought.popleft()
                gem_cnts[duplicate_gem] -= 1
                if gem_cnts[duplicate_gem] == 0:
                    answer_list.remove(duplicate_gem)
                if len(bought) > 0:
                    duplicate_gem = bought[0][0]
        bought.append((gem, i))
        
        if len(answer_list) == n_unique:
            diff = i - bought[0][1] 
            if best[1] - best[0] > diff:
                best = [bought[0][1]+1, i+1]
        
    return best

# solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA",])
# solution(["AA", "AB", "AC", "AA", "AC"])
# solution(["XYZ", "XYZ", "XYZ"])
solution(["A","B","B","B","B","B","B","C","B","A"])