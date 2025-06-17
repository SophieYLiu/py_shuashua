class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        p = q = 0

        """

        # best sol: 3 pointers | time O(n+m), space O(1)
        p1 = m - 1
        p2 = n - 1
        for p in range(n + m - 1, -1, -1):  # move p backwards, each time write the largest val pointed by p1 or p2
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

        # second best sol: 3 pointers | time O(n+m), space O(m)
        nums1_copy = nums1[:m]
        p1 = p2 = 0
        for p in range(n + m):
            if p2 >= n or (p1 < n and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

        # least best sol: sort
        # for i, num in enumerate(nums2):
        #     nums1[m+i] = num
        # nums1.sort()
