'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Eg
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque() # or list is fine too; use stack to store index; only allow val smaller coming in
        ans = [0]*len(temperatures)
        for cur_idx, cur_temp in enumerate(temperatures):
            # when current incoming is larger than top of stack value, pop top of stack, and calcaute ans for the poped indexed answer (as difference betweent the cur and poped index)
            while stack and temperatures[stack[-1]] < cur_temp:
                prev_idx = stack.pop()
                ans[prev_idx] = cur_idx - prev_idx
            # each cur is added to the stack
            stack.append(cur_idx)
        return ans
