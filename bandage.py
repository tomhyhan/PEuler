def solution(bandage, health, attacks):
    spell_t, base_r, spell_c = bandage
    hp = health
    max_hp = health
    start_t = 0
    for atk_t, atk_p in attacks:
        t = atk_t - start_t - 1
        hp_inc = t * base_r + (t // spell_t) * spell_c
        hp = min(max_hp, hp + hp_inc)
        hp -= atk_p
        
        start_t = atk_t
        if hp <= 0:
            return -1

    return hp

print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]]))