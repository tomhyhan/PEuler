import numpy as np

def is_prime(num):
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_rotate_prime(num):
    s_num = str(num)
    x = np.array(list(s_num))
    for _ in range(len(s_num)):
        current = int(''.join(x))
        if not is_prime(current):
            return False
        x = np.roll(x, 1)
    return True
    
def solution():
    cnt = 0
    for i in range(2,1000000):
        if is_rotate_prime(i):
            # print(i)
            cnt += 1
    print(cnt)
    
solution() 