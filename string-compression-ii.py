from math import inf
from functools import cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # knapsack
        @cache
        def dfs(i, rem, cur_count, prev):
            # if rem > 0, can only skip
            # compare delete vs skip, choose the shorter one
            # if cur_count == 1 or count will increase to 10**k, it increases the compression length as well
            if i == len(s): return 0

            if rem > 0:
                delete = dfs(i+1, rem-1, cur_count, prev)
            else:
                delete = inf
            
            if prev == s[i]:
                if cur_count == 1 or len(str(cur_count+1)) > len(str(cur_count)):
                    skip = 1 + dfs(i+1, rem, cur_count+1, s[i])
                else:
                    skip = dfs(i+1, rem, cur_count+1, s[i])
            else:
                skip = 1 + dfs(i+1, rem, 1, s[i])

            return min(skip, delete)
        
        return dfs(0,k,0,"")