def solution():
    l = 8
    of = [[0 for _ in range(l + 1)] for _ in range(l + 1)]

    for i in range(1, l+1):
        d = i + 1
        for j in range(0, i):
            n = j + 1
            of[i][j] = n / d

    print(of)

def bisect_numerator(target: tuple[int, int], denominator: int) -> int:
    target_numerator, target_denominator = target
    lower = 0
    upper = denominator * target_numerator // target_denominator
    print(denominator, upper)
    while lower < upper - 1:
        middle = (lower + upper) // 2 + 1
        if middle * target_denominator > target_numerator * denominator:
            upper = middle
        else:
            lower = middle
    return lower

def find_next_smaller_fraction(
    target: tuple[int, int], ceiling: int
) -> tuple[int, int]:
    target_numerator, target_denominator = target
    candidates = []
    for denominator in range(1, ceiling + 1):
        numerator = bisect_numerator(target, denominator)
    #     if numerator * target_denominator < target_numerator * denominator:
    #         numerator, denominator = reduce_fraction(numerator, denominator)
    #         candidates.append((numerator / denominator, numerator, denominator))
    # m = max(candidates)
    # return m[1:]
find_next_smaller_fraction((4,7), 8)
# solution()