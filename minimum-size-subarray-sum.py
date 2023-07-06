class Solution:
    def minSubArrayLen(self, tar: int, nums: List[int]) -> int:
        if sum(nums)<tar:
            return 0
        n = len(nums)
        res = n

        l,r=0,0
        total = 0
        while r<n:
            total += nums[r]

            if total>=tar:
                while l<=r and total-nums[l]>=tar:
                    total -= nums[l]
                    l+=1
                res = min(res,r-l+1)

            r+=1

        return res