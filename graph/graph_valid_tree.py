class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a valid tree should have n-1 edges
        if len(edges) != n - 1:
            return False
        # build bi-directed graph
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        nodes = list(graph.keys())

        if not nodes:
            return n == 1

        seen = set()

        # dfs
        def dfs(node, visited):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    dfs(child, visited)

        dfs(0, seen)
        return len(seen) == n

        # # bfs
        # q = collections.deque()
        # seen.add(nodes[0])
        # q.append(nodes[0])
        # while q:
        #     top = q.popleft()
        #     for child in graph.get(top, []):
        #         if child not in seen:
        #             q.append(child)
        #             seen.add(child)
        # return len(seen) == n


