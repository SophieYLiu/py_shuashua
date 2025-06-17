# DFS + mem
'''
n: len of s
m: len of dict
k: avg length of word in dict

Time complexity: O(n⋅m⋅k)
Spae: O(n)
'''
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    
    def dfs(i):
        if i == len(s):
            return True
        for j in range(i+1, len(s)+1): # 注意要到len(s) + 1 (别忘了加一)!
            s1 = s[i:j]
            if s1 in wordDict:
                if dfs(j):
                    return True
        return False

    return dfs(0)

# DP
''' 
Time complexity: O(n⋅m⋅k)
Spae: O(n)
'''
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [True] + [False]*n

    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[-1] 