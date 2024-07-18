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
   
def solution():
    tokens = tokenize()
    N = 10007

    card_pos = 1510
    visited = set()
    cnt = 0
    # while cnt < 3:
    for token in reversed(tokens):
        match token[0]:
            case 0:
                # increment
                inc_by = token[1]
                # card_pos = increment_card(card_pos, inc_by, N)
                # card_pos = (card_pos * pow(inc_by, -1, N)) % N 
                card_pos = pow(inc_by, N - 2, N)
            case 1:
                # new stack
                card_pos = back_new_stack(card_pos, N)
            case 2:
                # cut
                cut_by = token[1]
                card_pos = back_cut_card(card_pos, cut_by, N)
    cnt += 1
    print(card_pos)
    #  1 7 9 
    
    # Okay need to use fermat's little theorem ;)
    
    off = 0
    inc = 1
    card_pos = 2020
    N = 119315717514047
    times = 101741582076661
solution()



