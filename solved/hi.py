def solution(citations):
    citations.sort()
    N = len(citations)
    prev_h = 0
    for i in range(N):
        curr_n = N - i
        curr_h = citations[i]     
        if curr_n == prev_h:
            continue
        while curr_h > prev_h:
            # print(curr_h, curr_n, prev_h)
            if curr_n >= curr_h:
                break
            curr_h -= 1
        prev_h = curr_h
    # print(prev_h)
    citations.sort(reverse=True)
    print(list(enumerate(citations, start=1)))
    print(list(map(min, enumerate(citations, start=1))))
    return prev_h
solution([3, 0, 6, 1, 5])