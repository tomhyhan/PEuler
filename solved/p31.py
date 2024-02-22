def solution():
    coins = [1,2,5,10,20,50,100,200]
    s = 200
    n_ways = [0] * (s+1)
    n_ways[0] = 1
    for coin in coins:
        for i in range(s + 1):
            if coin <= i:
                n_ways[i] += n_ways[i-coin]
    # print(n_ways)

def helper(target, coins):
    s = 0 
    current_coin = coins[0]
    for i in range(10):
        pass

def solution2():
    coins = list(reversed([1,2,5,10,20,50,100,200]))
    helper(200, coins)

solution()
solution2()