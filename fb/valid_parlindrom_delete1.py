class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_parlindrom(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        n = len(s)
        i, j = 0, n-1
        while i < j:
            if s[i] != s[j]:
                return is_parlindrom(s, i, j-1) or is_parlindrom(s, i+1, j)
            i += 1
            j -= 1
        return True