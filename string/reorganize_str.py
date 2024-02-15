'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.



Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""

Solution Idea:
Alternate placing the most common letters.
Use PQ (max heap) to select the largest char with the largest count at each time
Note about the top 2 can have equal counts, and then you need check it
'''

import heapq, collections


class Solution:
    def reorganizeString(self, s: str) -> str:

        # order by negative value so that always first pop max (as max heap)
        pq = [(-cnt, ch) for ch, cnt in collections.Counter(s).items()]
        heapq.heapify(pq)

        res = ""
        while pq:
            top1_neg_cnt, top1_ch = heapq.heappop(pq)
            if res and res[-1] == top1_ch:
                if not pq: return ""
                top2_neg_cnt, top2_ch = heapq.heappop(pq)
                res += top2_ch
                if top2_neg_cnt + 1 != 0:
                    heapq.heappush(pq, (top2_neg_cnt + 1, top2_ch))
                heapq.heappush(pq, (top1_neg_cnt, top1_ch))
            else:
                res += top1_ch
                if top1_neg_cnt + 1 != 0:
                    heapq.heappush(pq, (top1_neg_cnt + 1, top1_ch))
        return res
