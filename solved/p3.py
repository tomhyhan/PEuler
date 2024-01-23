import numpy as np

def solution():
    arr = np.array([i for i in range(1, 101)]) 

    print(arr.sum() ** 2 - sum(arr ** 2))
    pass

solution()