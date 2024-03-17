import collections

# build graph (bi-dir) from list of edges
graph = collections.defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

# bfs - Note graph BFS needs visited/seen set
visited = set()
def bfs(start_node):
    queue = collections.deque()
    queue.append(start_node)
    visited.add(start_node)
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in visited:
                queue.append(nei)
                visited.add(nei)


# union find
def countComponents(self, n: int, edges: List[List[int]]) -> int:
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry 
    
    for x, y in edges:
        union(x, y)
    return len({find(i) for i in range(n)})

# union find (with rank)
def countComponents(self, n: int, edges: List[List[int]]) -> int:
    parent = list(range(n))
    rank = [1] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        if rank[rx] > rank[ry]:
            parent[ry] = rx
        elif rank[rx] < rank[ry]:
            parent[rx] = ry
        else:
            parent[rx] = ry
            rank[ry] += 1
    
    for x, y in edges:
        union(x, y)
    return len({find(i) for i in range(n)})


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build graph
        graph = collections.defaultdict(list)
        visited = set()
        # build 2-way (undirected) graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        if n == 0:
            return 0

        # bfs
        def bfs(start_node):
            queue = collections.deque()
            queue.append(start_node)
            visited.add(start_node)
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)

        cnt = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                cnt +=1
        return cnt

        # dfs: start with a node, and mark all reachables
        # def dfs(node):
        #     for nei in graph.get(node, []):
        #         if nei not in visited:
        #             visited.add(nei)
        #             dfs(nei)
        #
        # cnt = 0
        # for i in range(n):
        #     if i not in visited:
        #         cnt += 1
        #         dfs(i)
        #         visited.add(i)
        # return cnt