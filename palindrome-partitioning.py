class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # backtracking
        res = []
        temp = []
        def isPalin(i,j): # inclusive
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True

        def backtrack(i):
            if i>=len(s):
                res.append(temp.copy())
                return

            for idx in range(i, len(s)):
                if isPalin(i,idx):
                    temp.append(s[i:idx+1])
                    backtrack(idx+1)
                    temp.pop()
        
        backtrack(0)
        return res