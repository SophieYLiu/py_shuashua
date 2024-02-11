''' 
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Sol 1: time O(n), space O(1)
        # if len(s) != len(goal):
        #     return False
        # if len(s) == 0:
        #     return True
        # for i in range(len(s)):
        #     s = s[1:] + s[:1]
        #     if s == goal:
        #         return True
        # return False

        # Sol 2: time O(n), space O(1)
        return len(s) == len(goal) and goal in s + s

        # Sol 3:
        for i in range (len(s)):
            s = s[1:]+s[:1]
            if(s==goal):
                return True
        return False

# Sol 4: KPM
"""
KMP algorithm
time: O(N)
space: O(N)
"""

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if len(A) == 0: return True
        
        # capture length of strings
        # then make both strings 1 indexed
        N = len(A)
        A = " " + A + A
        B = " " + B
        
        # calculate pi table, it captures the length of the
        # longest prefix that is also the suffix
        pi = [0] * (N+1)
        left, pi[0] = -1, -1
        for right in range(1, N+1):
            while left >= 0 and B[left + 1] != B[right]:
                left = pi[left]
            left += 1
            pi[right] = left
        
        # do matching
        j = 0
        for i in range(1, (2*N)+1):
            while j >= 0 and B[j+1] != A[i]:
                j = pi[j]
            j += 1
            if j == N: return True
        
        return False