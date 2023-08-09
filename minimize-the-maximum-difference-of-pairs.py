class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if not p: return 0
        
        nums.sort()
        n = len(nums)
        l, r = 0, nums[-1]-nums[0]
        
        def isValid(m):
            i, cnt = 1, 0
            while i<n:
                if nums[i]-nums[i-1]<=m:
                    i+=2
                    cnt+=1
                else:
                    i+=1
                if cnt==p:
                    return True
            return False
        res = r 
        while l<=r:
            m = (l+r)//2
            if isValid(m):
                res = m
                r = m-1
            else:
                l = m+1
            
        return res