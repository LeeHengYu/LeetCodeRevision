class Solution:
    def rob(self, nums: List[int]) -> int:
        # either [0,n-1] or [1,n]
        res = 0
        n = len(nums)
        rob1, rob2 = 0, 0
        for i in range(n-1):
            # _R_(rob1) => _N_(rob2) => _R_
            # current state depends on previous two states
            new = max(rob1+nums[i], rob2)
            rob1 = rob2
            rob2 = new
        res=max(res, rob2)

        rob1, rob2 = 0, 0
        for i in range(1,n):
            new = max(rob1+nums[i], rob2)
            rob1 = rob2
            rob2 = new
        res=max(res, rob2)

        return max(res, nums[0])