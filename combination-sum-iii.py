class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # backtracking
        res = []
        def bt(i, total, cur):
            if total>n or (i==10 and total!=n): return
            if total==n:
                if len(cur)==k:
                    res.append(cur[:])
                return
            cur.append(i)
            bt(i+1, total+i, cur)
            cur.pop() # backtrack
            bt(i+1, total, cur)
        bt(1, 0, [])
        return res