"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
the key is use the map to record the address, (when add to map, just need to have the address and value, dont need to be complelty ready), use the dfs for loop to populate its neighbors/connections
need to use seen set

'''
from typing import Optional
class Solution:
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = set()
        graph_map = {}

        def dfs(node, seen):
            if not node: # forgot this, else line 26 have issues
                return None
            if node in seen and node in graph_map:
                return graph_map[node]
            if node not in graph_map:
                node_c = Node(node.val)
                graph_map[node] = node_c
            node_c = graph_map[node]
            for nei in node.neighbors:
                seen.add(nei)
                nei_c = dfs(nei, seen)
                node_c.neighbors.append(nei_c)
            return node_c
        
        return dfs(node, seen)