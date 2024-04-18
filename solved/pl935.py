class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        MEMO = {
            0 : [4, 6],
            1 : [8, 6],
            2 : [7, 9 ],
            3 : [4, 8],
            4 : [3, 9, 0],
            5 : [],
            6 : [1, 7, 0],
            7 : [2, 6],
            8 : [1, 3],
            9 : [2, 4]
        }
        
        DP = [1 for _ in range(10)]  
        
        for _ in range(n-1):
            new_dp = [0 for _ in range(len(DP))]
            for i in range(10):
                new_dp[i] = sum([DP[jump] for jump in MEMO[i]]) % mod
            DP = new_dp
        # print(sum(DP) % mod)s
        return sum(DP) % mod

# also solve recursive
s = Solution()
s.knightDialer(1)
s.knightDialer(2)
s.knightDialer(3)