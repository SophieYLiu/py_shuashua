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

'''
Given the root of a binary tree, turn the tree upside down and return the new root.
You can turn a binary tree upside down with the following steps:
 - rule1. The original left child becomes the new root.
 - rule2. The original root becomes the new right child.
 - rule3. The original right child becomes the new left child.
'''
def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def helper(node, parent=None, right=None):
        if not node:
            return parent  # 这里不是node哦
        newRoot = helper(node.left, node, node.right) # 最左边会是最后的新root, 最后return
        node.right = parent  # 右子是parent（被func传进来）(rule2)
        node.left = right  # 左子是parent的right（被func传进来） (rule3)
        return newRoot

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

# Invert BT (对折/mirror) 思路是从下往上，从最小的subtree开始换，然后再往上的大subtree换
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    # 关键：先到最右边，再到最左边，然后换 （也可以先到最左边，再到最右边，换）
    right = self.invertTree(root.right)
    left = self.invertTree(root.left)
    root.left = right
    root.right = left
    return root


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
    # 每个点（root）都做一次比较更新，然后决定向左走还是向右左
    closest = root.val
    while root:
        # closest = min(root.val, closest, key=lambda x: (abs(target-x), x))

        if abs(target - closest) > abs(target - root.val):
            closest = root.val
        elif abs(target - closest) == abs(target - root.val):  # often forgot this
            closest = min(closest, root.val)
        root = root.left if target < root.val else root.right
    return closest


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        # sol 1: get all numbers in list, and search them, and add. O(n) space and time
        # lst = []
        # def dfs(root, lst):
        #     if not root:
        #         return
        #     dfs(root.left, lst)
        #     lst.append(root.val)
        #     dfs(root.right, lst)

        # dfs(root, lst)
        # low_idx, high_idx = lst.index(low), lst.index(high)
        # return sum(lst[low_idx : high_idx+1])

        # sol2: more elegant
        ans = 0
        if not root:
            return 0
        if low <= root.val <= high:
            ans = root.val

        # range should be in the left subtree
        if low <= root.val or high <= root.val:
            ans += self.rangeSumBST(root.left, low, high)

        # range should be in the right subtree
        if root.val <= low or root.val <= high:
            ans += self.rangeSumBST(root.right, low, high)
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -math.inf

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            # forgot this! if there can be neg numbers, we need ignore the subtree result if it is neg
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            single_side_res = max(left, right) + node.val
            pass_root_res = left + right + node.val
            ans = max(ans, node.val, pass_root_res,
                      single_side_res)  # here need to compare multiple things. Easy to forgot "node.val" and "single_side_res"
            return single_side_res

        dfs(root)
        return ans

# BT longest consecutive seq
# need pass both cur node and its parent.The logic is 2-fold: continue count or start over
class Solution:
ans = 1
def longestConsecutive(self, root: Optional[TreeNode]) -> int:
    def dfs(node, parent, v):
        self.ans = max(v, self.ans)
        if not node:
            return
        if parent and node.val == parent.val + 1:
            # continue counting
            dfs(node.left, node, v + 1)
            dfs(node.right, node, v + 1)
        else:
            # start from fresh
            dfs(node.left, node, 1)
            dfs(node.right, node, 1)

    if not root:
        return 0
    dfs(root, None, 1)
    return self.ans

# Kth smallest in BST
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # easy sol: just print out in order
    # def helper(node, lst):
    #     if not node:
    #         return
    #     helper(node.left, lst)
    #     lst.append(node.val)
    #     helper(node.right, lst)
    # in_order_lst = []
    # helper(root, in_order_lst)
    # return in_order_lst[k-1]

    cnt = 0
    ans = None

    def dfs(node, k):
        nonlocal ans, cnt
        if not node:
            return

        # first go left, which starts with the smallest
        if node.left:
            dfs(node.left, k)

        # increment count
        cnt += 1
        if cnt == k:
            ans = node.val
            return

        # lastly go right
        if node.right:
            dfs(node.right, k)

    dfs(root, k)
    return ans

# Is same tree or subtree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same_tree(x, y):
            if not x and not y:
                return True
            if not (x and y):
                return False
            return x.val == y.val and is_same_tree(x.left, y.left) and is_same_tree(x.right, y.right)

        def dfs(root, sroot):
            if not root and not sroot:
                return True
            if not (root and sroot):
                return False

            if is_same_tree(root, sroot):
                return True
            if dfs(root.left, sroot):
                return True
            if dfs(root.right, sroot):
                return True
            return False

        return dfs(root, subRoot)

# BELOW for TREE PATH problems, we need use backtrack
# sum root to leaf numbers: convert path string to number and add eg 2 paths [1,2] and [1.3] => 12+13 = 25
class Solution:
    # key points: 其中一个base case是判断是不是leaf node（左右都是null）
    # edge case: [1,0], [9], [2,0,0], [1, null, 5]
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def path_to_num(lst):
            n = len(lst)
            num = 0
            for each in lst:
                num += each * int(math.pow(10, n - 1))
                n -= 1
            return num

        def dfs(node, path):
            if not node:
                return 0

            # in this block where we find a path - DONT ALTER PATH!
            if not node.left and not node.right:
                temp1 = list(path) + [node.val]  # cant use path.append(root.val) and then use path for num
                return path_to_num(temp1)

            ans = 0
            for child in [node.left, node.right]:
                path.append(node.val)  # here is node not child!!
                ans += dfs(child, path)  # here in recursive function is child
                path.pop()
            return ans

        return dfs(root, [])

# Binary Tree Paths
class Solution:
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