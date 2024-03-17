# interesting problem that even if it is not a sorted input, still can use binary search
def findPeakElement(self, nums: List[int]) -> int:
    l, r = 0, len(nums)-1
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] > nums[mid+1]:
            r = mid
        else:
            l = mid+1
    return l



"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


# Convert Binary Search Tree to Sorted Doubly Linked List
# Binary Search
def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right-left)//2
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# 1st bad version
def firstBadVersion(self, n: int) -> int:
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

# find min in ROTATED sorted array
class Solution:
    # min is the pivot point that divides into two
    # in the BS loop, first 找change points by comparing mid and before and after
    # next do 二分判断：mid 跟first_num比较
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]

        s = 0
        e = len(nums) - 1
        if nums[e] > nums[0]:
            return nums[0]

        while s < e:
            p = s + (e - s) // 2
            if nums[p] > nums[p + 1]: # change point at p+1
                return nums[p + 1]
            if nums[p - 1] > nums[p]: # change point at p
                return nums[p]
            # compare first and last element to know which side contains rotated
            if nums[p] > nums[0]:
                s = p + 1
            else:
                e = p - 1
        return s
