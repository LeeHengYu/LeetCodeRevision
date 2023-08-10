class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # if mid pointer is the same as left and right pointers, can't not proceed
        l,r=0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return True

            if nums[m]==nums[r]:
                r-=1
            elif nums[m]>nums[r]: # left half is sorted
                if nums[l]<=target and target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            else: # right half is sorted
                if nums[m]<target and target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
            
        return False