import heapq 

def solution(operations):
    min_hq = []
    max_hq = []
    
    for operation in operations:
        op, num = operation.split(' ')
        num = int(num)
        if op == 'I':
            heapq.heappush(min_hq, num)
            heapq.heappush(max_hq, -num) 
        else:
            if num == -1 and min_hq:
                heapq.heappop(min_hq)
                max_hq.pop()
            elif num == 1 and max_hq:
                heapq.heappop(max_hq) 
                min_hq.pop()

    return [-heapq.heappop(max_hq), heapq.heappop(min_hq)] if max_hq else [0,0]
# min -642
# max 45 -45 
solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
# [333, -45]
# solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])