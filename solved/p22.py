# ord('C') - ord('A') + 1

def solution():
    words = [w.strip('"') for w in open("./names.txt").read().split(',')]
    words.sort()
    total = 0
    for i, w in enumerate(words):
        worth = 0
        for c in w:
            worth += ord(c) - ord('A') + 1
        total += worth * (i + 1)
    print(total)

solution()