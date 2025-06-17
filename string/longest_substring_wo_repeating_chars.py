class Solution:

    # time O(n), space O(n)

    def lengthOfLongestSubstring_best(self, s: str) -> int:
        # i: start
        # j: end
        # if repeat detected: reset i (i=i+1), get max len
        if not s:
            return 0
        table = {}  # record previous characters appeared pos
        i = 0  # start pos
        ans = 1
        for j in range(len(s)):
            ch = s[j]
            if ch in table:
                ans = max(ans, j - i)
                i = max(i, table[ch] + 1)  # Key point 1!
            table[ch] = j
        ans = max(ans, len(s) - i)  # key point 2!
        return ans

    def lengthOfLongestSubstring_alt(self, s: str) -> int:
        if not s:
            return 0

        records = {}
        ans = 1
        i = 0
        n = len(s)
        # Key insight j doesnt need go back due to this info that (i, j) has uniq chars
        for j in range(n):  # loop j (end).
            cur = s[j]
            # gotta stop when repeat and reset the start
            if cur in records:
                i = max(records[cur], i)  # reset i (start)
            # calculate the ans at each loop
            ans = max(ans, j - i + 1)
            # log records
            records[cur] = j + 1

        return ans


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