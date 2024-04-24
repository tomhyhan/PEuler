import math

def solution():
    cnt = 0
    for n in range(7, 8):
        sq = math.sqrt(n)
        int_num = int(sq)
        denom = 1
        if sq.is_integer():
            continue
        result = []
        seen = []
        
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
            seen.append(state)
        print(seen)
        # print(n, result)
        if len(result) % 2 == 1:
            cnt += 1
    print(cnt)

def cont_faction(n):
    sq = math.sqrt(n)
    int_num = int(sq)
    denom = 1

    if sq.is_integer():
        raise Exception("asdf") 

    result = [int_num]
    seen = []
    
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
        seen.append(state)
    # print(result)
    return result
# solution()

# print("-------")
# print(expand_root(5))