# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_diameter(node):
            nonlocal diameter
            if not node:
                return 0
            left = longest_diameter(node.left)
            right = longest_diameter(node.right)
            cur = left + right
            diameter = max(diameter, cur)
            return max(left, right) + 1

        longest_diameter(root)
        return diameter