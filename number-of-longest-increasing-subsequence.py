class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {} # idx -> (lenLIS, cnt)
        res1, res2 = 0,0 # (lenLIS, cnt), global results
        for i in range(len(nums)-1,-1,-1):
            maxLen, maxCnt = 1, 1
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LEN, CNT = dp[j]
                    if LEN+1>maxLen:
                        maxLen, maxCnt = LEN+1, CNT
                    elif LEN+1==maxLen:
                        maxCnt += CNT

            dp[i] = (maxLen, maxCnt)
            if maxLen>res1:
                res1, res2 = dp[i]
            elif maxLen==res1:
                res2 += maxCnt

        return res2

        # NEETCODE sol: https://www.youtube.com/watch?v=Tuc-rjJbsXU