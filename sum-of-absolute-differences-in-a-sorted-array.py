class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = nums.copy()
        suffix = nums.copy()
        n = len(nums)
        for i in range(1, n):
            prefix[i] += prefix[i-1]
            suffix[n-1-i] += suffix[n-i]
        res = [0]*n
        res[0] = suffix[0] - nums[0]*n 
        res[n-1] = nums[n-1]*n - prefix[n-1]
        for i in range(1,n-1):
            res[i] = nums[i]*i - prefix[i-1] + suffix[i+1] - nums[i]*(n-1-i)
        return res