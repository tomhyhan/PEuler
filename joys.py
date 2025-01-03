# (13 - abs(ord(name[i]) - ord('N')))

def ways(name, n_As, back):
    total = 0
    for i in range(len(name)):
        curr_name = name[-i] if back else name[i]
        total += (13 - abs(ord(curr_name) - ord('N')))
        if len(name) - i == n_As:
            total -= 1
            break
        
        if i < len(name) - 1:
            total += 1
        
        if curr_name == 'A':
            n_As -= 1
    return total

def solution(name):
    n_As = name.count('A')
    
    if n_As == len(name):
        return 0
    
    ftotal = ways(name, n_As, False)
    btotal = ways(name, n_As, True)
    return ftotal if ftotal < btotal else btotal

print(solution("BABA"))
# solution("JAN")
# solution("JAZ")
# solution("JZA")
# solution("JEROEN")