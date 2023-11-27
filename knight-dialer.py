class Solution:
    def knightDialer(self, n: int) -> int:
        mapping = {
            0: [4,6],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [3,9,0],
            5: [],
            6: [0,1,7],
            7: [2,6],
            8: [1,3],
            9: [2,4],
        }
        mod = 10**9+7
        @cache
        def dfs(prev, l):
            if l == n: return 1
            v = sum([dfs(x, l+1) for x in mapping[prev]])
            return v%mod
        return sum([dfs(x, 1) for x in range(10)])%mod