class Solution:
    def sumOfSquares(self, nums) -> int:
        n = len(nums) 
        res = 0
        nums = [0]+nums
        print(nums)
        for i in range(1,floor(n**0.5)+1):
            if n%i==0:
                res += nums[i]**2
                if i!=n//i:
                    res += nums[n//i]**2
                
        return res