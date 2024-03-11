from collections import defaultdict
keys="""319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716"""
def solution():
    weights = defaultdict(int)
    seens = defaultdict(int)
    key_list = keys.split('\n')
    for key in key_list:
        w = 3
        for c in key:
            weights[c] += w
            seens[c] += 1
            w -= 1
    password = []
    for k in weights:
        password.append([k, weights[k] / seens[k]])
    password.sort(key=lambda x: x[1], reverse=True)
    print(''.join([p[0] for p in password]))

def solution2():
    key_list = keys.split('\n')
    first = set()
    s = set()
    for key in key_list:
        if '7' in key:
            key = key[1:]
        first.add(key[0])
        s.add(key[1])
    print(s)
    print(first)
    print(first - s)
    pass

solution()
solution2()