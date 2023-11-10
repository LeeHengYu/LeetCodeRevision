from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        visit = set()
        for u,v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)
        
        root = None
        for node, ls in adj.items():
            if len(ls)==1:
                root = node
                break
        
        res = []
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            res.append(node)
            for nxt in adj[node]:
                if nxt not in visit:
                    dfs(nxt)
        dfs(root)
        return res