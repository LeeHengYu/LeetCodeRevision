class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # standard backtracking
        res = []

        def dfs(cur, idx):
            if len(cur)==k:
                res.append(cur.copy())
                return
            
            for num in range(idx,n+1):
                cur.append(num)
                dfs(cur, num+1)
                cur.pop()
            
        dfs([],1)
        return res