class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        n = len(cost)
        @cache
        def dp(i, walls: int) -> int:
            if walls<=0: return 0
            if i>=n: return inf

            paid = dp(i+1, walls-1-time[i]) + cost[i]
            skip = dp(i+1, walls)
            return min(paid, skip)

        return dp(0,n)