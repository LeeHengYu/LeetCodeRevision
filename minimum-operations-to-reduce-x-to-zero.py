class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums)-x
        # find the longest subarray s.t. the sum is target
        res = -1
        l = r = 0
        n = len(nums)
        total = 0
        while r<n:
            total += nums[r]
            # 3 cases
            # if total < target: continue
            # if total == target: update
            # if total > target: move l pointer
            while l<n and total>target:
                total -= nums[l]
                l += 1
            if total==target:
                res = max(r-l+1, res)
            r += 1
        return -1 if res==-1 else n-res