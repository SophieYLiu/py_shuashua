# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):  # left and right cant be declared as TreeNode
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


# a few notes:
# 0) when print path, pass temp in the recursive fun, and return type is void
# 1) pass empty temp in the entry point function,
# 2) in the backtrack, add and pop the current node val, and in the middle recursive call pass the child node
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(node, t_sum, temp):
            if not node:
                return

            if not node.left and not node.right and t_sum == node.val:
                res.append(temp + [node.val])
                # return # if return here wont be able to pop out

            # backtrack
            for child in [node.left, node.right]:
                temp.append(node.val)  # add current node
                dfs(child, t_sum - node.val, temp)  # recurse into child
                temp.pop()

        # entry point
        res = []
        dfs(root, targetSum, [])
        return res

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, tsum):
            if not node:
                return False
            if not node.right and not node.left and tsum == node.val:
                return True

            return any(dfs(child, tsum - node.val) for child in [node.left, node.right])

        return dfs(root, targetSum)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(node, temp):
            if not node:
                return

            if not node.left and not node.right:
                temp1 = list(temp) + [node.val]
                temp_str = "->".join([str(each) for each in temp1])
                res.append(temp_str)

            for child in [node.left, node.right]:
                temp.append(node.val)
                dfs(child, temp)
                temp.pop()

        res = []
        dfs(root, [])
        return res