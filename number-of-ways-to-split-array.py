class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # split at index i means there are i+1 elements on the left
        n = len(nums)
        total = 0
        prefix = []
        for num in nums:
            total += num
            prefix.append(total)

        res = 0
        for cut in range(n-1):
            if prefix[-1]-prefix[cut] <= prefix[cut]:
                res += 1

        return res
