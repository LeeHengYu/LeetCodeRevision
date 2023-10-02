from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        res = 0
        n = len(values)

        adj = defaultdict(list)
        for u,v,_ in edges:
            adj[u].append((v,_))
            adj[v].append((u,_))

        visited = {0}
        # backtracking
        def dfs(node, quality, timeCost): # totalValue initial = values[0]
            nonlocal res
            if not node: res = max(res, quality)
            for nei, time in adj[node]:
                newTime = timeCost + time
                if newTime > maxTime: continue
                seen = nei in visited # not the first visit
                visited.add(nei)
                dfs(nei, quality+(values[nei] if not seen else 0), newTime)
                if not seen: visited.remove(nei)
        dfs(0,values[0],0)
        return res