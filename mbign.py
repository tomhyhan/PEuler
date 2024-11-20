class Num:
    def __init__(self, num):
        self.num = str(num)
        
    def __lt__(self, other_num):
        smaller = int(self.num + other_num.num) < int(other_num.num + self.num) 
        return False if smaller else True
    
    def __len__(self):
        return len(self.num)
    
    def __repr__(self):
        return f"{self.num}"
def cmp_fn(a,b):
    print(a,b)
    return a < b

def solution(numbers):
    print(sorted(numbers, key=cmp_fn))
    numbers = [Num(n) for n in numbers]
    # print(''.join([c.num for c in sorted(numbers, reverse=True)]))
    answer = ''.join([c.num for c in sorted(numbers)])
    return 0 if answer[0] == '0' else answer


solution([3, 30, 34, 5, 9])