from collections import defaultdict
import heapq

def solution(genres, plays):
    memo = defaultdict(int)
    orders = defaultdict(list)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        memo[genre] += play
        heapq.heappush(orders[genre], (-play, i))
    result = []
    for genre, _ in sorted(memo.items(), key=lambda x: -x[1]):
        for _ in range(2):
            if orders[genre]:
                p, id_ = heapq.heappop(orders[genre])
                result.append(id_)
    print(result)
    return result

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])

solution(["classic", "classic", "classic", "classic", "pop"], [50, 60, 100, 30, 8000])