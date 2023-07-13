class Solution:
    def canFinish(self, n: int, prereq: List[List[int]]) -> bool:
        # topo sort
        adj = [[] for _ in range(n)]
        for crs, pre in prereq:
            adj[pre].append(crs)
        
        visit, cycle = set(), set()
        def dfs(node):
            if node in visit:
                return True
            if node in cycle:
                return False

            cycle.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            cycle.remove(node)
            visit.add(node)
            return True

        for i in range(n):
            if not dfs(i):
                return False
        return True