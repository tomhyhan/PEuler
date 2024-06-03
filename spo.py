def solution(a, s):
    
    bs = []
    ka = 0
    for ke in s:
        sub_a = [[num] for num in a[ka:ka+ke]]
        bs.append(sub_a)
        ka = ka+ke

    for b in bs:
        ways = helper(b, 0)
        print(ways, )
        break        

def helper(b, i):
    if i >= len(b):
        return 1
    
    # print(b, i)
    ways = 0
    if i-1 < 0 or sum(b[i])!= sum(b[i-1]):
        ways += helper(b, i+1) 
    
    if i > 0 and sum(b[i]) == sum(b[i-1]):
        new_b = b[:i-1] + [b[i-1] + b[i]] + b[i+1:]
        print(b)
        print(new_b, i)
        ways += helper(new_b, i)
        # return 
    return ways

solution([1,1,1,1,1,1,2,5,8,2,1,1,4,8,8,8,12,6,6], [4,3,1,5,6])