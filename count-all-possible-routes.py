class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # DP with memorization using caching
        cache = {}

        def dfs(current, remain):
            if remain < 0:
                return 0
            if (current, remain) in cache:
                return cache[(current, remain)]
            res = 0
            if current == finish:
                res += 1
            for i in range(len(locations)):
                if i != current:
                    res += dfs(i, remain -
                               abs(locations[i]-locations[current]))
            cache[(current, remain)] = res % (10**9+7)
            return cache[(current, remain)]

        dfs(start, fuel)
        return cache[(start, fuel)] % (10**9+7)
