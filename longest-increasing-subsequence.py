class Solution1: # O(n*n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
    
    
class Solution2: #O(nlogn)
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            if not res or n>res[-1]:
                res.append(n)
            else:
                idx = bisect_left(res,n)
                res[idx]=n
        return len(res)