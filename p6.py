import time

def is_palin(snum):
    num_len = len(snum)
    for i in range(len(snum) //2):
        if snum[i] != snum[num_len-i-1]:
            return False
    return True

# brute force
# def solution():
#     max_p = 0
#     for i in range(100,1000):
#         for j in range(100,1000):
#             num = i * j
#             if (is_palin(str(num))):
#                 max_p = max(max_p, num)
#     print(max_p)

# bit smarty
def solution():
    # 100000a + 10000b + 1000c + 100c + 10b + a  
    # 100001a + 10010b + 1100c
    # 11(9091a * 910b * 100c)
    max_p = 0
    for i in range(100,1000):
        for j in range(110,991,11):
            num = i * j
            if (is_palin(str(num))):
                max_p = max(max_p, num)
    print(10010 // 11)
    print(max_p)

start_time = time.time()
solution()
end_time = time.time()
print("Execution time: ", f"{end_time - start_time:.2f}", "seconds")

# 0.37 bf 
# 0.03 divisible by 11 => 
