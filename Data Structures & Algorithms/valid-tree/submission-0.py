class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check if valid tree first
        if len(edges) != n-1:
            return False



        graph = {}
        for i in range(n):
            graph[i] = []
        # graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for neighbor in graph[node]:
                # found other pair
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n