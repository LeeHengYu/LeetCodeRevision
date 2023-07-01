class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        dist = [0]*k
        n = len(cookies)
        res = 8*10**5
        # Enumerate all possibilities: backtracking
        def backtrack(i):
            nonlocal res
            if i==n:
                res = min(res, max(dist)) 
                return

            for j in range(k):
                dist[j]+=cookies[i]
                if max(dist)<res: # still possible to update res downwards
                    backtrack(i+1)
                dist[j]-=cookies[i] # try out next person

        cookies.sort(reverse=True) # avoid unnecessary backtracking
        backtrack(0)
        return res