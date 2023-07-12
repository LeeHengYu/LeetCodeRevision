class Solution:
    def eventualSafeNodes(self, adj: List[List[int]]) -> List[int]:
        # backward DFS - topological sort
        n = len(adj)
        visit, cycle = set(), set()
        def dfs(node):
            # 3 states:
            # unvisted - not added into visit nor cycle
            # visited - it's added into output
            # visiting - it's in the cycle but not in visit
            
            if node in visit:
                return True
            if node in cycle:
                return False

            cycle.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            cycle.remove(node)
            visit.add(node)
            return True

        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res   