class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # DP memorization
        n = len(s)
        dp = [0]*(n+1)
        temp = ""
        for i, c in enumerate(s):
            temp += c
            res = dp[i]+1
            for word in dictionary:
                offset = len(word)
                if temp.endswith(word):
                    res = min(res, dp[i+1 - offset])
            dp[i+1] = res

        return dp[-1]
