class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        table = [-1] * 1000
        res, start = 1, 0
        for i in range(n):
            letter_pos = ord(s[i])
            if table[letter_pos] != -1:
                res = max(res, (i-start))
                print(s[start:i])
                start = max(start, table[letter_pos]+1) # 另一个重点. "tmmzuxt" test case. (if use 'start+1' then wrong. Needs to be 'start')
            table[letter_pos] = i # 这一句要在if外面，不管什么情况每个loop都要记录
        res = max(res, n-start) # “au” test case
        return res