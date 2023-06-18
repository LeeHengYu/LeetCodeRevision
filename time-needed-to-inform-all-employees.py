from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        adj = defaultdict(list)
        for i, m in enumerate(manager):
            if i == headID:
                continue
            adj[m].append(i)

        visit = set()

        def dfs(em):
            maxTime = 0
            if em not in adj:
                return 0

            for sub in adj[em]:
                maxTime = max(maxTime, dfs(sub))

            return informTime[em] + maxTime

        return dfs(headID)
