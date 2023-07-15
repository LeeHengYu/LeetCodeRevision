class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        mod = 10**9 + 7
        
        l, r= 0, n-1
        count=0
        while l<=r:
            if nums[l]+nums[r]>target:
                r-=1
            else:
                # we must pick left
                count += pow(2,r-l,mod)
                l+=1
        return count%mod