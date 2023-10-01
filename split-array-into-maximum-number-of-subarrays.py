class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        M = 2**20-1
        lowest = nums[0]
        for n in nums:
            lowest &= n
        # if the lowest value is not 0, then cannot split
        # reasoning: if split, there will be one more array with a score >= 1
        if lowest: return 1

        # greedy split
        cur = M
        res = 0
        for n in nums:
            cur &= n
            if not cur:
                res += 1
                cur = M
        return res