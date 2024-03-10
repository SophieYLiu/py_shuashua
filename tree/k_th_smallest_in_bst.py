# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Need to finish all traversal, and log in middle. => Cant directly return at line 16 (wont work)
# so need 2 global vars
class Solution:
    def helper(self, node, k):
        if not node:
            return
        self.helper(node.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.res = node.val
            return node.val
        self.helper(node.right, k)
        return -1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.res = 0
        self.helper(root, k)
        return self.res



# Sol 2
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node, lst):
            if not node:
                return
            helper(node.left, lst)
            lst.append(node.val)
            helper(node.right, lst)

        in_order_lst = []
        helper(root, in_order_lst)
        return in_order_lst[k - 1]