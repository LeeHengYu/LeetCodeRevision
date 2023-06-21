class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        diff = 10**9
        for i in range(n-1):
            diff = min(diff, nums[i+1]-nums[i])

        return diff
