import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    n_mix = 0
    while len(scoville) >= 2 and scoville[0] < K :
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)

        mix = f + s*2
        heapq.heappush(scoville, mix)
        n_mix += 1

    return n_mix if scoville[0] >= K else -1

solution([1, 2, 3, 9, 10, 12], 7)