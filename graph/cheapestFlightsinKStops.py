class Solution:
    # DFS不用seen； 用mem记得是2d：node和stop
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(int)
        for s, d, price in flights:
            if s not in graph:
                graph[s] = []
            graph[s].append((d, price))
        

        def dfs(node, stops, mem):
            if node == dst:
                return 0
            if stops < 0:
                return float('inf')
            if (node, stops) in mem:
                return mem[(node, stops)]
            min_so_far = float('inf')
            for child, price in graph.get(node, []):
                min_so_far = min(min_so_far, dfs(child, stops-1, mem) + price)
            mem[(node, stops)] = min_so_far
            return min_so_far
        
        mem = {}
        res = dfs(src, k, mem)
        return res if res != float('inf') else -1