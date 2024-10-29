from collections import defaultdict, Counter

def solution(a):
    
    counter = Counter(a)
    longest = 0
    
    for num, cnt in counter.items():
        if longest > cnt:
            continue
        
        i=0
        stars = 0
        while i < len(a)-1:
            if a[i] != a[i+1] and (a[i] == num or a[i+1] == num):
                i += 2
                stars += 1
                continue
            i += 1
        longest = max(longest, stars)
    # print(longest)
    return longest * 2


def solution(a):
        
    pass



# 0110
# 110
# 011
# [5,2,3,3,5,3] -> wrong
    
# solution([0,3,3,0,7,2,0,2,2,0,0])
solution([0,3,3,0,7,2,0,2,2,0])
solution([5,2,3,3,5,3])
# solution([0])