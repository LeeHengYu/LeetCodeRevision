class Solution:
    def longestSubsequence(self, arr: List[int], dif: int) -> int:
        dp = {}
        for n in arr:
            dp[n]=dp.get(n-dif,0)+1
        return max(dp.values())