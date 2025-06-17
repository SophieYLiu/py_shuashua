def findPeakElement(self, nums: List[int]) -> int:
    # best sol: time O(logn), space O(1)
    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] > nums[mid + 1]:  # mid in the descreasing slope => look left
            r = mid
        else:  # mid in the increasing slope => look right
            l = mid + 1
    return l

    # easiest: basically search for the largest val (linear scan: time O(n), space O(1))
    # return nums.index(max(nums))