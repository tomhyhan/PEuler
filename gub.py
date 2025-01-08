
def solution(people, limit):
    people.sort()
    
    left = 0
    right = len(people) - 1
    
    while right > 0 and people[left] + people[right] > limit:
        right -= 1
    
    n_matchings = 0
    while left < right:
        if people[left] + people[right] > limit:
            right -= 1
            continue
        left += 1
        right -= 1
        n_matchings +=1
        
    return len(people) - 2 * n_matchings + n_matchings 

print(solution([70, 50, 80, 50], 100))
print(solution([6, 2, 6, 2], 100))