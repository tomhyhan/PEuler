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

def cut_card(card_pos, cut_by, N):
    return (card_pos - cut_by) % N   
   
def solution():
    
    tokens = tokenize()
    N = 119315717514047 
    cards = [n for n in range(N)]
    answer = [-1 for n in range(N)]

    card_pos = 2020
    for token in tokens:
        match token[0]:
            case 0:
                # increment
                inc_by = token[1]
                card_pos = increment_card(card_pos, inc_by, N)
            case 1:
                # new stack
                card_pos = new_stack(card_pos, N)
            case 2:
                # cut
                cut_by = token[1]
                card_pos = cut_card(card_pos, cut_by, N)
        # if i == 3:
        #     print(card_pos)
        # answer[card_pos] = cards[i]
    # 0 3 6 9 2 5 8 1 4 7
    print(card_pos)

solution()


