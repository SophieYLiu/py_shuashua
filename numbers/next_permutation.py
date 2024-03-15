class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return nums

        # find first non-increasing segment's start from backwards: i (peak num)
        n = len(nums)
        i = n - 1
        while i - 1 >= 0 and nums[i] <= nums[i - 1]:
            i -= 1

        anchor = nums[i - 1]
        if i - 1 >= 0:
            # going back in that descending segment[i, n-1], also in backwards, to find first num bigger than (i-1): j
            j = n - 1
            while j >= i and nums[j] <= anchor:
                j -= 1

            # swap i-1, j
            print(i - 1, j)

            nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # reverse (i, end)
        p, q = i, n - 1
        while p < q:
            nums[p], nums[q] = nums[q], nums[p]
            p += 1
            q -= 1
        return nums