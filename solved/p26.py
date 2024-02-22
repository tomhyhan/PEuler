def is_cycle(num):
    divide_by = 10
    seen = {}
    i = 0
    while True:
        _, remainder = divmod(divide_by, num)
        if remainder == 0:
            return False
        if remainder in seen:
            return i - seen[remainder]
        seen[remainder] = i
        divide_by = remainder * 10
        i += 1

def solution():
    max_cycle = 0
    for num in range(2, 1000):
        if (cycle_n := is_cycle(num)):
            if max_cycle < cycle_n:
                max_cycle = cycle_n 
                print("num", num)
    print(max_cycle)

solution()