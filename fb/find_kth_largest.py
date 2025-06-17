class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # bes sol: count sort (time O(n+m), space O(m))

        # ok sol: min heap (time O(n*logk), space O(k))
        if not nums:
            return -1

        import heapq
        pq = []
        for ele in nums:
            heapq.heappush(pq, ele)
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]

        # Sol: quick select
        # def swap(nums, i, j):
        #     temp = nums[i]
        #     nums[i] = nums[j]
        #     nums[j] = temp

        # def partition(nums, s, e):
        #     pivot = nums[e]
        #     i = s
        #     for j in range(i, e): # easy to be wrong - start from i to e-1 (coz we take the last (e) as pivot)
        #         if pivot > nums[j]: # if condition is for anything large than pivot, -> then out of order should move back
        #             swap(nums, j, i)
        #             i += 1
        #     swap(nums, i, e)
        #     return i

        # n = len(nums)
        # s, e = 0, n-1
        # while s <= e:
        #     idx = partition(nums, s, e)
        #     if idx == n-k: # key issue: kth largest == (n-k)th in ascending ordered list
        #         return nums[idx]
        #     if idx > n-k:
        #         e = idx-1
        #     else:
        #         s = idx+1
        # return -1

        # Sol: count sort | time O(n+m), space O(m) where n: len of nums, m: max - min (num buckets)
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1

        remain = k
        for num in range(len(count) - 1, -1, 1):
            remain -= count[num]
            if remain <= 0:
                return num + min_value
        return -1