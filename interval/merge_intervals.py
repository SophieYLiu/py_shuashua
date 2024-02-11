''' 
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        def overlap(itv1, itv2):
            assert itv1[0] <= itv2[0]
            if itv1[1] >= itv2[0]:
                return [itv1[0], max(itv1[1], itv2[1])]
            return None

        intervals.sort()
        merged = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            itv = intervals[i]
            overlapped = overlap(merged, itv)
            if overlapped:
                merged = overlapped
            else:
                res.append(merged)
                merged = itv
        
        res.append(merged)
        return res