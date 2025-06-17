"""
root-to-leaf path sum equals to targetSum
"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, tsum):
            if not node:
                return False
            if not node.right and not node.left and tsum == node.val:
                return True

            return any(dfs(child, tsum - node.val) for child in [node.left, node.right])

        return dfs(root, targetSum)

""" 
all of the result
"""
class Solution1:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(root, tsum, temp):
            if not root:
                return
            if tsum == root.val and not root.left and not root.right:
                res.append(list(temp) + [root.val])
            for child in [root.left, root.right]:
                temp.append(root.val)
                dfs(child, tsum-root.val, temp)
                temp.pop()
        dfs(root, targetSum, [])
        return res