class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = {0:0, 1:0}
        l,r=0,0
        res = 0
        while r<len(nums):
            count[nums[r]]+=1
            r+=1
            if count[0]==2:
                while count[0]==2 and l<r:
                    count[nums[l]]-=1
                    l+=1

            else:
                if count[0]==1:
                    res = max(res, count[1])
                else:
                    res = max(res, count[1]-1)

        return res