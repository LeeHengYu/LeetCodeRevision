class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        res = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]%2==0:
                res[l] = nums[i]
                l+=1
            else:
                res[r] = nums[i]
                r-=1
        return res