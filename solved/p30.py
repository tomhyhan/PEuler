def solution():
    total = 0
    for num in range(32,354294):
        sn = sum(map(lambda x: int(x) ** 5, list(str(num))))
        if num == sn:
            print(num)
            total += num
    print(total)
solution()