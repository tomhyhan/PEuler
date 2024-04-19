import math

def solution():
    cnt = 0
    for x in range(2, 10000):
        x = math.sqrt(x)
        x = x - int(x)
        
        if x == 0:
            continue

        seen = set()
        while True:
            x = 1 / x 
            x = x - int(x)
            key = round(x, 9)
            if key in seen:
                break
            seen.add(key)
        # print(seen)
        if len(seen) % 2 == 1:
            cnt += 1
    print(cnt)
def expand_root(number: int) -> tuple[list[int], list[int]]:
    floor = int(math.sqrt(number))
    if floor**2 == number:
        return [floor], []
    results = [floor]
    states = [(1, floor)]
    c = floor
    b = 1
    print(floor, c, b)
    while True:
        # print()
        assert c > 0
        # print(f"{b}/(sqrt({number}) - {c})")
        d = number - c**2
        print("d", d)
        gcd = math.gcd(b, d)
        # print(f"{b} (sqrt({number}) + {c})/{d}")
        b //= gcd
        d //= gcd
        # print(f"{b} (sqrt({number}) + {c})/{d}")
        split = (floor + c) // d
        a = split * b
        c -= split * d
        # print(f"{a} + {b} (sqrt({number}) + {c})/{d}")
        c = -c
        b = d
        state = (b, c)
        results.append(a)
        if state in states:
            break
        states.append(state)
    i = states.index(state) + 1
    return results[:i], results[i:]

def solution() -> int:
    result = 0
    for number in range(23, 24):
        beginning, period = expand_root(number)
        if len(period) % 2 == 1:
            result += 1
    print(result)
    return result
solution()