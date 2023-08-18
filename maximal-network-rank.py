from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(set)
        for u,v in roads:
            adj[u].add(v)
            adj[v].add(u)
        res = 0
        for i, rds1 in adj.items():
            l1= len(rds1)
            for j, rds2 in adj.items():
                if i==j:
                    continue
                l2 = len(rds2)
                if i in rds2:
                    res = max(res, l1+l2-1)
                else:
                    res = max(res, l1+l2)
        return res