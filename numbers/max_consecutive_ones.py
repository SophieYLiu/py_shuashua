# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
def longestOnes(self, nums: List[int], k: int) -> int:
    left, right = 0, 0
    n = len(nums)
    for right in range(n):
        # reduce window k if there is '0'
        if nums[right] == 0:
            k -= 1
        # bump to constraint that all k steps consumed， and move left
        if k < 0:
            k += 1 # +1 => so that left can keep move next;
            if nums[left] == 1:
                k -= 1 # to discount for when the left side of is 1
            left += 1
    return right - left + 1