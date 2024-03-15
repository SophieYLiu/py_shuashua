# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
思路：转化成graph，然后层搜
'''
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        # convert the tree to graph
        graph = collections.defaultdict(list)
        node = root
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            left, right = node.left, node.right
            if left:
                graph[node].append(left)
                graph[left].append(node)
                q.append(left)
            if right:
                graph[node].append(right)
                graph[right].append(node)
                q.append(right)

        # do BFS
        q.append(target)
        visited = set()  # need to have visited since the graph is bi-directional (even if there isnt cycle)
        visited.add(target)
        while q:
            if k == 0:
                return [each.val for each in q]
            sz = len(q)
            for i in range(sz):
                node = q.popleft()
                for child in graph[node]:
                    if child not in visited:
                        q.append(child)
                        visited.add(child)
            k -= 1
        return []


