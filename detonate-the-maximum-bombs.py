import math


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        N = len(bombs)
        adj = [[] for i in range(N)]
        for i in range(N):
            x1, y1, r1 = bombs[i]
            for j in range(i+1, N):
                x2, y2, r2 = bombs[j]
                d = math.sqrt((x1-x2)**2+(y1-y2)**2)
                if d <= r1:
                    adj[i].append(j)
                if d <= r2:
                    adj[j].append(i)

        # DFS
        res = 0

        def dfs(i, visit):
            # recursion
            if i in visit:
                return

            visit.add(i)
            for nei in adj[i]:
                dfs(nei, visit)

            return len(visit)

        for i in range(N):
            res = max(res, dfs(i, set()))

        return res
