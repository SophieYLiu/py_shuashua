class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        # import heapq
        # pq = []
        # for ele in nums:
        #     if len(pq) >= k and ele > pq[0]:
        #         heapq.heappop(pq)
        #         heapq.heappush(pq, ele)
        #     elif len(pq) < k:
        #         heapq.heappush(pq, ele)
        # return pq[0]

        def partition(nums, s, e):
            pivot = nums[e]
            i = s
            for j in range(i, e):  # easy to be wrong - start from i to e-1 (coz we take the last (e) as pivot)
                if pivot > nums[
                    j]:  # if condition is for anything large than pivot, -> then out of order should move back
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[e] = nums[e], nums[i]
            return i

        n = len(nums)
        s, e = 0, n - 1
        while s <= e:
            idx = partition(nums, s, e)
            if idx == n - k:  # key issue: kth largest == (n-k)th in ascending ordered list
                return nums[idx]
            if idx > n - k:
                e = idx - 1
            else:
                s = idx + 1
        return -1
