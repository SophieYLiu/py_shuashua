'''
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation:
All possible ways to reach at index 3 with value 0 are:
index 5 -> index 4 -> index 1 -> index 3
index 5 -> index 6 -> index 4 -> index 1 -> index 3
'''

from typing import List
import collections
class Solution:
    # didnt come to me to add visited, and got inf recursion
    def canReach_DFS(self, arr: List[int], start: int) -> bool:

        def dfs(pos, arr, visited):
            if pos < 0 or pos >= len(arr):
                return False
            if pos in visited:
                return False
            if arr[pos] == 0:
                return True

            visited.add(pos)

            if dfs(pos + arr[pos], arr, visited):
                return True
            if dfs(pos - arr[pos], arr, visited):
                return True
            return False

        return dfs(start, arr, set())

    def canReach_BFS(self, arr: List[int], start: int) -> bool:
        q = collections.deque()
        q.append(start)
        visited = set()

        while q:
            cur = q.popleft()
            if arr[cur] == 0:
                return True
            visited.add(cur)
            for node in [cur + arr[cur], cur - arr[cur]]:
                if 0 <= node < len(arr) and node not in visited:
                    q.append(node)
        return False
