def solution():
    # a + b + c = 120
    # c = 120 - (a + b)
    # a ** 2 + b ** 2 = c ** 2
    # a**2 + b**2 = (120-a-b)**2
    # 14400 − 240a − 240b + 2ab = 0
    # 7200 - 120a - 120b + ab = 0
    # a**2 + b**2 = p**2 - 2pa - 2pb + a**2 + 2ab + b**2
    # p**2 - 2pa - 2pb + 2ab = 0
    # b = p(p-2a) / 2(p-a)
    # for p in range(2, 1001, 2):
    p = 120
    max_cnt = 0
    num = 0
    for p in range(2,1001, 2):
        cnt = 0
        for a in range(1,p):
            b = (p * (p - 2*a)) / (2 * (p-a))
            if int(b)== b:
                cnt += 1
            if a > b:
                break
        if cnt > max_cnt:
            max_cnt = cnt
            num = p
    print(max_cnt, num)
solution()