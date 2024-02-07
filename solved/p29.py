def solution():
    seen = set()
    for a in range(2, 101):
        for b in range(2, 101):
            num = a ** b
            if num in seen:
                continue
            seen.add(num)
    print(len(seen))

solution()