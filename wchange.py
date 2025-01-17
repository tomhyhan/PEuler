import heapq

def solution(begin, target, words):
    words = set(words)
    queue = [(0, begin)]

    seen = set()
        
    while queue:
        n_changes, word = heapq.heappop(queue)
        
        if word in seen:
            continue
        seen.add(word)
        
        if word == target:
            return n_changes
        
        for i in range(len(word)):
            for aval in range(ord('a'), ord('z')+1):
                char = chr(aval)
                new_word = word[:i] + char + word[i+1:]
                if new_word in words:
                    heapq.heappush(queue, (n_changes+1, new_word))

    return 0

# def helper(n_change, word, seen, words, target):
#     if word == target:
#         return n_change
    
#     min_changes = float('inf')
#     for i in range(len(word)):
#         for aval in range(ord('a'), ord('z')+1):
#             char = chr(aval)
#             new_word = word[:i] + char + word[i+1:]
#             if new_word not in seen and new_word in words:
#                 seen.add(new_word)
#                 curr_chagnes = helper(n_change+1, new_word, seen, words, target)
#                 min_changes = min(min_changes, curr_chagnes)
#                 seen.remove(new_word)
    
#     return min_changes

# def solution(begin, target, words):
#     min_changes = helper(0, begin, set(), set(words), target)
#     return min_changes if min_changes != float('inf') else 0  

# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))