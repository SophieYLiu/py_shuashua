"""
Given 2 lists (I think they are sorted), and find intersections

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        # O((m+n)*log(m+n))
        # combined = sorted(firstList+secondList)
        # intersection = []
        # currentEnd = -1

        # for start, end in combined:
        #     if start <= currentEnd:
        #         intersection.append([start, min(currentEnd, end)])
        #     currentEnd = max(currentEnd, end)
        # return intersection

        # O(m+n)
        ans = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans