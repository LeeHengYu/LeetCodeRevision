from bisect import bisect_right

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        # consider every element as the starting point
        # check how many elements we can include in the range without changing anything
        res = n-1 # worst case
        for i, startNum in enumerate(nums):
            rightBound = bisect_right(nums, startNum+n-1)
            res = min(res, n - (rightBound-i))
        return res