'''
Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def helper(node, parent=None, right=None):
        if not node:
            return parent  # 这里不是node哦
        res = helper(node.left, node, node.right)
        node.right = parent  # 右子是parent（被func传进来）
        node.left = right  # 左子是parent的right（被func传进来）
        return res

    return helper(root, None, None)


# Validate BTS
'''
Rules:
1. left subtree of a node contains only nodes whose values less than the node
2. right subtree of a node contains only nodes whose values greater than the node
Both the left and right subtrees must also be binary search trees.
'''
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def dfs(root, low, high):
        # for left child: (root.root, root)
        # for right child: (root, cur.right)
        if not root:
            return True
        if not (low < root.val < high):
            return False
        # 一下两句弄不对。。。 low high parameters这块。。
        valid_L = dfs(root.left, low, root.val)
        valid_R = dfs(root.right, root.val, high)
        return valid_L and valid_R

    return dfs(root, float('-inf'), float('inf'))

# Invert BT (对折/mirror)
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    # 关键：先到最右边，再到最左边，然后换 （也可以先到最左边，再到最右边，换）
    right = self.invertTree(root.right)
    left = self.invertTree(root.left)
    root.left = right
    root.right = left
    return root


# LCA
def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    # If looking for me, return myself
    if root == p or root == q:
        return root

    left = right = None
    # else look in left and right child
    if root.left:
        left = self.lowestCommonAncestor(root.left, p, q)
    if root.right:
        right = self.lowestCommonAncestor(root.right, p, q)

    # if both children returned a node, means
    # both p and q found so parent is LCA
    if left and right:
        return root
    else:
        # either one of the chidren returned a node, meaning either p or q found on left or right branch.
        # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
        # somewhere below node where 'p' was found we dont need to search all the way,
        # because in such scenarios, node where 'p' found is LCA
        return left or right

# Invert BT (对折/mirror)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # 关键：先到最右边，再到最左边，然后换 （也可以先到最左边，再到最右边，换）
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root