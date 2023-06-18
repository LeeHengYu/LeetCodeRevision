class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        front, end = 0, 0
        n = len(nums)
        res = []
        while end < n:
            while end+1 < n and nums[end+1] == nums[end]+1:
                end += 1

            if front != end:
                res.append(str(nums[front])+"->"+str(nums[end]))
            else:
                res.append(str(nums[end]))
            front, end = end+1, end+1

        return res
