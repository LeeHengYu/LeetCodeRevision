class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # DP
        n = len(cost)
        cache = {}  # this caching the min cost incurred at that step

        def solve(i, tc, w):  # this returns the total cost
            if (i, w) in cache:
                return cache[(i, w)]+tc
            if w <= 0:
                return tc
            if i >= n:
                return inf

            paid = solve(i+1, tc+cost[i], w-time[i]-1)
            free = solve(i+1, tc, w)

            cache[(i, w)] = min(paid, free)-tc
            return min(paid, free)

        return solve(0, 0, n)

    # Sol: https://leetcode.com/problems/painting-the-walls/solutions/3655230/line-by-line-explanation-for-dummies-like-me/
