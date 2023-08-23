class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def bt(ans, nums):
            n = len(nums)
            if not nums:
                res.append(ans)
                return
            for i in range(n):
                if i>0 and nums[i-1]==nums[i]:
                    continue
                bt(ans+[nums[i]], nums[:i]+nums[i+1:])
        bt([],nums)
        return res