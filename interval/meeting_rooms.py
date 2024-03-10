''' 
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

'''
import heapq
class Solution:
    # First of all - need sort interval by start time
    # 双指针（pq记录history开始的meetings，另外一个iterate到下一个即将开的meeting）
    # 1） 如果能free a room， 也就是pq里最早结束的meeting房间可以给现在要开的meeting，那么就free掉（pq.pop)
    # 2） 不能free any, 说明都被占用
    # 最后len(pq)就是需要的房间，即同时需要的
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        pq = []
        heapq.heappush(pq, intervals[0][1]) # push the first end time

        # 有点类似双指针，一个hp，一个list
        for itv in intervals[1:]:
            if pq[0] <= itv[0]: # smallest end time in pq <= cur start (can free a room)
                heapq.heappop(pq) # free a room
            heapq.heappush(pq, itv[1]) # add to pq (log a room)
        return len(pq)