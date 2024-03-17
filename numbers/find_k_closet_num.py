class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # Sol 0. heap: O(k*logk)
        # import heapq
        # pq = []
        # # O(n*logk)
        # for num in arr:
        #     dist = abs(num-x)
        #     heapq.heappush(pq, [-dist, num])
        #     if len(pq) > k:
        #         heapq.heappop(pq)

        # res = [each[1] for each in pq]
        # return sorted(res)

        # Sol 1: just sort by dist: O(nlogn)
        # sorted_arr = sorted(arr, key=lambda num: abs(x-num))
        # return sorted(sorted_arr[:k])

        # Sol 2: BS + sliding win
        if len(arr) == k:
            return arr

        # init window
        left = bisect_left(arr, x) - 1
        right = left + 1

        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        return arr[left + 1:right]