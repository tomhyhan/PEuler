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
    
def increment_card(card_pos, inc_by, N):
    return (card_pos * inc_by) % N


def new_stack(card_pos, N):
    return N - card_pos - 1 

def back_new_stack(card_pos, N):
    return N - card_pos - 1 

def cut_card(card_pos, cut_by, N):
    return (card_pos - cut_by) % N   

def back_cut_card(card_pos, cut_by, N):
    return (card_pos + cut_by) % N
   
def mod_inv(inc_by, N):
    return pow(inc_by, N - 2, N)

def solution():
    tokens = tokenize()

    card_pos = 0
    # card_pos = 2020
    # N = 119315717514047
    N = 10
    times = 101741582076661
    off = 0
    inc = 1
    # while cnt < 3:
    for token in reversed(tokens):
        match token[0]:
            case 0:
                # increment
                inc_by = token[1]
                pinv = pow(inc_by, N-2,N)
                inc *= pinv
                off *= pinv
            case 1:
                # new stack
                off += 1
                inc *= -1
                off *= -1
                print(off, inc )
            case 2:
                # cut
                cut_by = token[1]
                off += cut_by
        inc %= N
        off %= N
    print(-1 % 10)
    # print((
    #     pow(inc, times, N) * card_pos +
    #     off * (pow(inc, times, N) +N- 1)
    #       * (pow(inc-1, N - 2, N))
    # ) % N)
        
solution()



