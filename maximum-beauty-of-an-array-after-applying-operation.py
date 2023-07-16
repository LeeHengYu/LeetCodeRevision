class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = 1
        right = 0
        for i in range(n):
            while right < n and nums[right]-nums[i]<=2*k:
                right += 1
            res = max(res, right-i)
            if right==n:
                break
        return res