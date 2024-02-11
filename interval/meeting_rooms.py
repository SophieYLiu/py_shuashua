''' 
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

'''
class Solution:
    # 只要有overlap就log一个room (换句话就是只要不overlap就从pq里poll一个出来)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        pq = []
        heapq.heappush(pq, intervals[0][1]) # push the first end time

        prev = intervals[0]
        for itv in intervals[1:]:
            if pq[0] <= itv[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, itv[1])
        return len(pq)