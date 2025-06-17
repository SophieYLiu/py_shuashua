"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        dic = {'a', 'e', 'i', 'o', 'u'}

        # init the window [0 ~ k-1]
        count = 0
        for i in range(k):
            count += int(s[i] in dic)
        answer = count

        # gradually move right
        for i in range(k, len(s)):
            count += int(s[i] in dic)
            count -= int(s[i-k] in dic)
            answer = max(answer, count)

        return answer