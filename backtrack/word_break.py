# time complexity: O(n^2) because the total computation is basically filling up the DP table
# without using memorization, the dfs takes O(n^(m/k)), where n is the num of words in dict, m is the total len of input string, and k is average words in dict.
class Solution:
    """
    eg.
    Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
    Output: ["cats and dog","cat sand dog"]
   """
    def wordBreak_II(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(start, temp):
            if start == len(s):
                res.append(" ".join(temp))
            for j in range(start, len(s)+1):  # 注意要到len(s) + 1 (别忘了加一)!
                if s[start:j] in wordDict:
                    temp.append(s[start:j])
                    dfs(j, temp)
                    temp.pop()
        res = []
        dfs(0, [])
        return res

   """ 
    n: len of s
    m: len of dict
    k: avg length of word in dict
    
    Time complexity: O(n⋅m⋅k)
    Spae: O(n)


   eg.
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".
   """
    def wordBreak_I_DFS_w_MEM(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def dfs(start):
            if start == len(s):
                return True
            for j in range(start, len(s)+1):
                if s[start:j] in wordDict and dfs(j):
                    return True
            return False
        return dfs(0)

    def wordBreak_I_DP(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False]*n

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]