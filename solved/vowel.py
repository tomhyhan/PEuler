from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for perm in product(list("AEIOU"), repeat=i):
            words.append(perm)
    words = {''.join(w):i for  i, w in enumerate(sorted(words))}
    print((5 ** (5 - 0) - 1) / (5 - 1) * "AEIOU".index('E') + 1)
    return words[word] + 1
# 6
solution("AAAAE")
# 10
solution("AAAE")


