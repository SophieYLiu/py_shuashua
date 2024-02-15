# time complexity: O(n^2)
class Solution:
    def wordBreak_II(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(start, temp):
            if start == len(s):
                res.append(" ".join(temp))
            for j in range(start, len(s)+1):
                if s[start:j] in wordDict:
                    temp.append(s[start:j])
                    dfs(j, temp)
                    temp.pop()
        res = []
        dfs(0, [])
        return res

    def wordBreak_I(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def dfs(start):
            if start == len(s):
                return True
            for j in range(start, len(s)+1):
                if s[start:j] in wordDict and dfs(j):
                    return True
            return False
        return dfs(0)