import math

def sum_divisors(num):

    total = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            total += (i + num // i) if i*i != num else i 
    return total - num 
    
def solution():
    abundants = []

    for i in range(12, 28123 - 12 + 1):
        if sum_divisors(i) > i:
            abundants.append(i)
            
    abundants_sums = set()
    for a in abundants:
        for b in abundants:
            if (a + b <= 28123):
                abundants_sums.add(a + b)
    print(sum([n for n in range(28123 + 1) if n not in abundants_sums]))
solution()