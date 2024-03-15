# Given a string s, return the number of palindromic substrings in it.
class Solution:
    def countSubstrings(self, s: str) -> int:

        def middle_out(i_, j_, s_):
            cnt = 0
            while i_ >= 0 and j_ < len(s) and s[i_] == s[j_]:
                i_ -= 1
                j_ += 1
                cnt += 1
            return cnt

        ans = 0
        for i in range(len(s)):
            ans += middle_out(i, i, s)
            ans += middle_out(i, i + 1, s)
        return ans

    # another
    def countSubstrings(self, s: str) -> int:

        ans = 0
        sz = len(s)
        dp = [[0 for _ in range(sz)] for _ in range(sz)]

        # # fill out forwards
        # for j in range(sz):
        #     for i in range(0, j+1):
        #         if i == j:
        #             dp[i][j] = 1
        #         elif i + 1 == j and s[i] == s[j]:
        #             dp[i][j] = 1
        #         elif s[i] == s[j] and i+1 <= j-1:
        #             dp[i][j] = dp[i+1][j-1]
        #         else:
        #             dp[i][j] = 0
        #         ans += dp[i][j]

        # fill out from backwards
        for i in reversed(range(sz)):
            for j in range(i, sz):
                if i == j:
                    dp[i][j] = 1
                elif i + 1 == j and s[i] == s[j]:
                    dp[i][j] = 1
                elif s[i] == s[j] and i + 1 <= j - 1:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 0
                ans += dp[i][j]
        return ans



def countSubstrings(self, s: str) -> int:
    def middle_out(i_, s_):
        cnt = 0
        p, q = i_, i_
        while p >= 0 and q < len(s_):
            # not a parlindrom
            if s_[p] != s_[q]:
                return cnt

            # skip two invalid cases: 1) '#' 2) '#[ANY_CHAR]#'
            if s_[p: q + 1] != '#' and not (s_[p: q + 1].startswith('#') and s_[p: q + 1].endswith("#")):
                cnt += 1

            # next iteration
            p -= 1
            q += 1

        return cnt

    res = 0
    s = '#'.join([ch for ch in s])  # re-construct string to have special token in between
    for i in range(len(s)):
        res += middle_out(i, s)
    return res