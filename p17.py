import math

def solution():
    cnt = 0
    for n in range(2, 10_000):
        sq = math.sqrt(n)
        int_num = int(sq)
        denom = 1
        if sq.is_integer():
            continue
        result = []
        seen = set()
        
        while True:
            new_denom = n - int_num**2

            gcd = math.gcd(denom, new_denom)
            denom //= gcd
            new_denom //= gcd
            
            split = int((sq + int_num) // new_denom)
            int_part = split * denom
            remainder = int_num - split * new_denom


            int_num = -remainder
            denom = new_denom
            state = (denom, int_num)
            if state in seen:
                break
            result.append(int_part)
            seen.add(state)
        # print(n, result)
        if len(result) % 2 == 1:
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
        print('split, a, b, c, d' )
        print(split, a, b, c, d)
        # print(f"{a} + {b} (sqrt({number}) + {c})/{d}")
        c = -c
        b = d
        state = (b, c)
        results.append(a)
        if state in states:
            break
        states.append(state)
    print("state", states)
    print("results", results)
    i = states.index(state) + 1
    return results[:i], results[i:]


solution()

# print("-------")
# print(expand_root(5))