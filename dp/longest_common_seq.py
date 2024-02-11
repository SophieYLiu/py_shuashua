class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # @lru_cache(maxsize=None)
        # def dfs(i, j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
            
        #     op1 = dfs(i+1, j) # not include or skip the current i-th

        #     op2 = 0 # include current i-th
        #     idx = text2.find(text1[i], j)
        #     if idx != -1:
        #         op2 = 1 + dfs(i+1, idx+1)
            
        #     return max(op1, op2)

        # return dfs(0, 0)

        # DP solution: 谁在inner or outer loop无所谓，注意是从后往前填所以reversed，分两种情况
        n, m = len(text1), len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
