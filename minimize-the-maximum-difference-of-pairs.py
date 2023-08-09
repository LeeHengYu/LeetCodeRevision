class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        l,r=0,nums[-1]-nums[0]
        while l<r:
            mid = (l+r)//2
            k,i=0,1 # current pair, index reached
            while i<n:
                if nums[i]-nums[i-1]<=mid:
                    k+=1
                    i+=1
                i+=1 # jump to new pair
            if k>=p: # valid, if total number of pairs with the difference <= mid is more than p
                # reduce the target res, but mid can also be the ans
                r=mid # real difference can be smaller
            else:
                l=mid+1
        return min(l, r)