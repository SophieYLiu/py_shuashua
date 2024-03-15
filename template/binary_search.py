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

# is BST
