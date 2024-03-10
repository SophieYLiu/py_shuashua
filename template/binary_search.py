def findPeakElement(self, nums: List[int]) -> int:
    l, r = 0, len(nums)-1
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] > nums[mid+1]:
            r = mid
        else:
            l = mid+1
    return l


''' 
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

=> basically needs to find the largest distance from a node to 2 leafs 
'''
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    diameter = 0

    def longest_path(node):
        if not node:
            return 0
        nonlocal diameter

        left = longest_path(node.left)  # longest path from current node to a leaf in the left subtree
        right = longest_path(node.right)  # longest path from current node to a leaf in the right subtree

        diameter = max(diameter, left + right)
        return max(left, right) + 1

    longest_path(root)
    return diameter


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


# Convert Binary Search Tree to Sorted Doubly Linked List
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(node):
            nonlocal last, first
            if not node:
                return

            dfs(node.left)

            if last:
                # link the prev node (last) with the cur one
                last.right = node
                node.left = last
            else:
                first = node
            last = node

            dfs(node.right)

        first, last = None, None
        dfs(root)

        # close DLL
        last.right = first
        first.left = last
        return first


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # In order to get the lst, and then procee: O(n) time and space
        # def in_order(node, lst):
        #     if not node:
        #         return
        #     in_order(node.left, lst)
        #     lst.append(node.val)
        #     in_order(node.right, lst)

        # lst = []
        # in_order(root, lst)

        # three ways to find the min
        # way 1.
        # import numpy as np
        # idx = np.argmin(np.array([abs(each-target )for each in lst]))
        # return lst[idx]

        # way 2.
        # return min(lst, key=lambda x: abs(target-x))

        # way 3.
        # res = (0, math.inf)
        # for i, val in enumerate(lst):
        #     if abs(val-target) <= res[1]:
        #         res = (i, abs(val-target))
        # return lst[res[0]]

        # Binary search: O(H) time and O(1) space
        closest = root.val
        while root:
            # closest = min(root.val, closest, key=lambda x: (abs(target-x), x))

            if abs(target - closest) > abs(target - root.val):
                closest = root.val
            elif abs(target - closest) == abs(target - root.val):  # often forgot this
                closest = min(closest, root.val)
            root = root.left if target < root.val else root.right
        return closest