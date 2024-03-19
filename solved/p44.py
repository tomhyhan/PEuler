def solution():
    pens = []
    for n in range(1, 10000):
        pen = n * (3 * n - 1) // 2
        pens.append(pen)
    print(7042750 - 1560090)
    for i in range(len(pens)):
        for j in range(i + 1, len(pens)):
            f, s = pens[i], pens[j]
            if is_pen(pens, abs(s - f)) and is_pen(pens, s + f):
                print(f,s)

def is_pen(pens, target):
    left = 0
    right = len(pens) - 1
    while left <= right:
        mid = (left + right) // 2
        if pens[mid] > target:
            right = mid - 1
        elif pens[mid] < target:
            left = mid + 1
        else:
            return True

    return False

solution()