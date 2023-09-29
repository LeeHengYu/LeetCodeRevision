class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)<=2: return True 
        opt = nums[0]
        inc = None
        for n in nums:
            if inc==None:
                if n>opt: inc=True
                elif n<opt: inc=False
                opt=n
                continue
            
            if (inc and n<opt) or (not inc and n>opt): return False
            opt = max(opt, n) if inc else min(opt, n)
        return True