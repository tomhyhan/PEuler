from collections import defaultdict
import math

def create_seller(sellers, amounts):
    seller = {}
    for s, a in zip(sellers, amounts):
        seller[s] = a * 100
    return seller

def create_ddg(enroll, referral):
    ddg = defaultdict(list)
    
    for e, r in zip(enroll, referral):
        if r == '-':
            r = "center"
        ddg[r].append(e)
    return ddg
        
def solution(enroll, referral, seller, amount):
    ddg = create_ddg(enroll, referral)
    seller = create_seller(seller, amount)

    profits = {}
    helper("center", ddg, seller, profits)
    # print(profits)
    result = []
    for person in enroll:
        result.append(profits[person])
    return result

def helper(name, ddg, seller, profits):
    profit = 0
    
    for s in ddg[name]:
        profit += helper(s, ddg, seller, profits)

    if name in seller:
        profit += seller[name]
        
    if profit < 10:
        profits[name] = profit
        return 0
    
    margin = math.ceil(profit * 0.9)
    rest = math.floor(profit * 0.1)
    profits[name] = margin

    return rest 

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10])

# solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["sam", "emily", "jaimie", "edward"],[2, 3, 5, 4])