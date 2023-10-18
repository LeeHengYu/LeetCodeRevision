from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # topo sort
        deg = [0]*(n+1)
        adj = defaultdict(list)
        for u,v in relations:
            deg[v]+=1
            adj[u].append(v)

        # BFS
        dist = [0] + time
        q = [i for i in range(1,n+1) if deg[i]==0]
        while q:
            course = q.pop(0)
            for nxt in adj[course]:
                dist[nxt] = max(dist[nxt], dist[course]+time[nxt-1])
                deg[nxt] -= 1
                if deg[nxt] == 0:
                    q.append(nxt)
        return max(dist)