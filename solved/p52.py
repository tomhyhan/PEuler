from collections import Counter

def solution():
    # 199
    for i in range(3,20):
        num = 10 ** i
        end = int(10 ** i / 0.6)
        for n in range(num, end + 1):
            if Counter(str(n)) == Counter(str(2*n)) == Counter(str(3*n)) == Counter(str(4*n)) == Counter(str(5*n)):
                print("n", n)
                return

def solution2():
    print(str(1/7)[2:8])

solution()
solution2()