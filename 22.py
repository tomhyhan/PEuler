def tokenize():
    with open("input.txt") as f:
        lines = f.read().split('\n')
        tokens = []
        for line in lines:
            if line.startswith("deal with increment"):
                tokens.append((0, int(line.split()[3])))
            elif line.startswith("deal into new stack"):
                tokens.append((1, 0 ))
            elif line.startswith("cut"):
                tokens.append((2, int(line.split()[1])))
            else:
                raise Exception("??")
    return tokens

from math import gcd

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse exists for {a} and {m}")
    else:
        return x % m

def find_x(y, inc_by, N):
    g = gcd(inc_by, N)
    if y % g != 0:
        raise ValueError(f"No solution exists because gcd({inc_by}, {N}) does not divide {y}")

    # Reduce the equation by gcd
    inc_by_reduced = inc_by // g
    N_reduced = N // g
    y_reduced = y // g

    # Find the modular inverse of the reduced inc_by
    inverse_inc_by = mod_inverse(inc_by_reduced, N_reduced)
    
    # Compute one solution
    x0 = (y_reduced * inverse_inc_by) % N_reduced

    # Generate all solutions
    solutions = [(x0 + i * N_reduced) % N for i in range(g)]
    
    return solutions[0]

def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean(b % a, a)
        return gcd, y - (b // a) * x, x

def modular_inverse(a, m):
    gcd, x, _ = extended_euclidean(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def solve_congruence(y, inc_by, N):
    try:
        inv_inc_by = modular_inverse(inc_by, N)
        x = (y * inv_inc_by) % N
        return x
    except Exception as e:
        return f"Error: {str(e)}"
    
    
def increment_card(card_pos, inc_by, N):
    return (card_pos * inc_by) % N

def back_increment_card(card_pos, inc_by, N):
    print(inc_by)
    inverse_mod = pow(inc_by, -1, N)
    return  (card_pos * inverse_mod) % N

def new_stack(card_pos, N):
    return N - card_pos - 1 

def back_new_stack(card_pos, N):
    return N - card_pos - 1 

def cut_card(card_pos, cut_by, N):
    return (card_pos - cut_by) % N   

def back_cut_card(card_pos, cut_by, N):
    return (card_pos - cut_by) % N
   
def solution():
    tokens = tokenize()
    N = 10007 

    card_pos = 1510
    for token in tokens:
        match token[0]:
            case 0:
                # increment
                inc_by = token[1]
                # card_pos = increment_card(card_pos, inc_by, N)
                # card_pos = back_increment_card(card_pos, inc_by, N)
                # card_pos = solve_congruence(card_pos, inc_by, N)
                card_pos = find_x(card_pos, inc_by, N)
            case 1:
                # new stack
                card_pos = back_new_stack(card_pos, N)
            case 2:
                # cut
                cut_by = token[1]
                card_pos = back_cut_card(card_pos, cut_by, N)
        # if i == 3:
        #     print(card_pos)
        # answer[card_pos] = cards[i]
    # 0 3 6 9 2 5 8 1 4 7
    # deal with increment 7
    # Result: 0 3 6 9 2 5 8 1 4 7
    # print(back_increment_card(1, 7, 10))
    print(card_pos)

solution()



# Example usage:
try:
    y = 2020       # example value
    inc_by = 64    # example increment value
    N = 10007      # example modulus
    solutions = find_x(y, inc_by, N)
    print(f"The possible values of x are: {solutions}")
except ValueError as e:
    print(e)
