import numpy as np

def solution():
    print(np.array([i for i in range(1,1000) if i % 3 == 0 or i % 5 == 0]).sum())
solution()