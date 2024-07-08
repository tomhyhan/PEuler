import re

def helper(user_id, banned_id, visited, banned_list):
    if len(banned_id) == 0:
        if visited in banned_list:
            return 0
        banned_list.append({v for v in visited})
        
        return 1

    result = 0
    ban = banned_id.pop()    
    for user in user_id:
        if user in visited:
            continue 
        if re.fullmatch(ban, user):
            visited.add(user)
            result += helper(user_id, banned_id, visited, banned_list)
            visited.remove(user)
    banned_id.append(ban)
    
    return result

def solution(user_id, banned_id):
    for i in range(len(banned_id)):
        banned_id[i] = banned_id[i].replace('*', ".")
    banned_list = []
    result = helper(user_id, banned_id, set(), banned_list)
    return result
from itertools import product

def check(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == "*":
            continue
        if str1[i] != str2[i]:
            return False
    return True

def solution(user_id, banned_id):
    answer = set()
    result = [[] for i in range(len(banned_id))]

    for i in range(len(banned_id)):
        for u in user_id:
            if check(banned_id[i], u):
                result[i].append(u)

    result = list(product(*result))
    print(result)
    
# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], 
#          ["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], 
         ["*rodo", "*rodo", "******"])
# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], 
#          ["fr*d*", "*rodo", "******", "******"])