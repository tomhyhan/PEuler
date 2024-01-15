import numpy as np
import math

def is_prime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if (num % i ==0):
            return False
    return True

def solution():
    num = 600851475143
    for i in range(1,int(math.sqrt(num)+1)):
        if (num % i == 0) and is_prime(i):
            print(i)

solution()