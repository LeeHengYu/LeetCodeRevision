class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # dp (similar to coin change)
        def checkDup(s):
            return len(s) == len(set(s))

        res = 0
        unique = [''] # base case
        for s in arr:
            for prev in unique:
                new = prev+s
                if checkDup(new):
                    res = max(res, len(new))
                    unique.append(new)
        return res
    
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # bit manipulation needed for sure (for alphabet)
        # backtracking
        res = 0
        def dfs(i, mask, stringLen):
            nonlocal res
            if i == len(arr):
                res = max(stringLen, res)
                return

            # knapsack?
            dfs(i+1, mask, stringLen)

    # if there is no duplication in current string and after including it, include it and dfs
            a = 0
            for c in arr[i]:
                interDup = a & 1 << (ord(c) - ord('a'))
                if interDup:
                    return
                a |= 1 << (ord(c) - ord('a'))
            if a & mask:
                return
            mask |= a
            dfs(i+1, mask, stringLen+len(arr[i]))
        dfs(0,0,0)
        return res