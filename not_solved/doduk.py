def solution(money):
    cf = money[:-1]
    cs = money[1:]
    
    cf[1] = cf[0]
    cs[1] = max(cs[0], cs[1])
    
    for i in range(2, len(money)-1):
        cf[i] = max(cf[i-1], cf[i] + cf[i-2])
        cs[i] = max(cs[i-1], cs[i] + cs[i-2])
    print(cs, cf)
    return max(cs[-1], cf[-1])

# f 1
# s 2
# f=max(2<s>,1<f>+3) s=f, f=s
# f=max(4<s>,2<f>+1) 
# 4
# 1 100
# 
print(solution([5,10,100,50]))
# solution([1, 2, 3, 1])
# print(solution([2,1,5]))
# print(solution([2,1,1,5]))
# print(solution([10,1,5]))
# print(solution([1000, 10, 10, 2000, 30]))
# print(solution([10, 1000, 10, 62, 2000]))
# solution([1, 0, 2, 3, 1])