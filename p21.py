import math

def sum_divisors(num):
    total = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            total += (i + num // i) if i ** 2 != num else i
    return total

def solution():
    amicable = {}
    total = 0
    for num in range(2, 10000):
        dsum = sum_divisors(num)
        if num in amicable and amicable[num] == dsum:
            total += (num + amicable[num])
        else:
            amicable[dsum] = num
    print(total)
solution()