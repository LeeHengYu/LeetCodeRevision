# brute force from min(nums) to max(nums), or num in nums: TLE
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)

        def calc(tar):
            ans = 0
            for num, c in zip(nums, cost):
                ans += abs(num-tar)*c
            return ans

        # Hard to know 2 things:
        # 1. it is optimal to change the numbers to one already in the array (Hint)
        # 2. Binary Search is a solution: need to know that the cost is V-shaped curve
        # (However, we do know that the target number is between the min and the max of array, which kinda provides the idea.)

        l, r = min(nums), max(nums)

        while l < r:
            m = (l+r)//2
            if calc(m) > calc(m+1):
                l = m+1
            else:
                r = m
        return min(calc(l), calc(r))
