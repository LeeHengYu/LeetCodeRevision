from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        ct = Counter(nums)
        deg = max(ct.values())
        l,r = 0,0
        cur = {}
        tempMax = 0
        res = len(nums)
        while r<len(nums):
            cur[nums[r]] = cur.get(nums[r], 0)+1
            while cur[nums[r]]==deg:
                res = min(res, r-l+1)
                cur[nums[l]] -= 1
                l+=1
            r+=1
        return res