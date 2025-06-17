"""
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # best sol: time O(n), space O(1)
        i, j = 0, len(s)-1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

        # sol of time O(n), space O(n)
        # s = [ch.lower() for ch in s if ch.isalnum()]
        # return s == list(reversed(s))