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