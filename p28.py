import numpy as np

def distance(a, b):
    return abs(a) + abs(b)

def solution():
    total = 1
    s_diagnols = 1
    left = 0
    right = 2
    while distance(left, right) + 1 <= 1001:
        d = distance(left, right)
        ct = 0
        for _ in range(4):
            s_diagnols += d
            ct += s_diagnols
            total += s_diagnols
        left -= 1
        right += 1
    print(total)

def get_diagnol(s, x):
    return s[0] * x ** 2 + s[1] * x + s[2]

def solution2():
    x_values = np.array([3, 5, 7])
    y_values = np.array([24, 76, 160])

    coefficients = np.polyfit(x_values, y_values, deg=2)

    total = 0
    for x in range(3, 1002, 2):
        total += get_diagnol(coefficients, x)
    print(int(total + 1))

solution()
solution2()