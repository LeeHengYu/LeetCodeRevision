class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[-1] = True
        for i in range(n-1,-1,-1):
            for w in wordDict:
                if i+len(w)<=n and s[i:i+len(w)]==w and dp[i+len(w)]:
                    dp[i] = True
                    break
        return dp[0]