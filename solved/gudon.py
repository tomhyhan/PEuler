def solution(n, money):
    MOD =  1_000_000_007
    DP = [0] * (n + 1)
    DP[0] = 1
    for m in money:
        for change in range(1, n+1):
            if m <= change:
                DP[change] += DP[change-m] % MOD
    return DP[-1]
solution(5, [1,2,5])

def solution(n, money):
    MOD = 1_000_000_007

    def count_ways(amount, index, memo):
        if amount == 0:
            return 1
        if amount < 0 or index == len(money):
            return 0
        if memo[amount][index] != -1:
            return memo[amount][index]
        
        print(amount, money[index])
        print(amount, index)
        print()
        # Include the current coin
        include_coin = count_ways(amount - money[index], index, memo) % MOD
        # Exclude the current coin
        exclude_coin = count_ways(amount, index + 1, memo) % MOD
        # print(include_coin)
        # print(exclude_coin)
        # print()
        memo[amount][index] = (include_coin + exclude_coin) % MOD
        return memo[amount][index]

    # Initialize memoization table with -1
    memo = [[-1] * len(money) for _ in range(n + 1)]
    
    return count_ways(n, 0, memo)

solution(5, [1,2,5])
