from collections import defaultdict

def solution(genres, plays):
    total_a = defaultdict(int)
    songs = defaultdict(list)
    
    for id, (genre, play) in enumerate(zip(genres, plays)):
        total_a[genre] += play
        songs[genre].append((id, play))
    
    result = []
    for genre, _ in sorted(total_a.items(), key=lambda x: x[1], reverse=True):
        song_list = songs[genre]
        ids = [id for id, _ in sorted(song_list, key= lambda x: (x[1], -x[0]), reverse=True)[:2]]
        result.extend(ids)

    return result
    # print(result)        
# [4, 1, 3, 0]
solution(["classic", "pop", "classic", "classic", "pop"], [150, 600, 150, 800, 2500])
