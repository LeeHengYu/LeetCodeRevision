class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        ***Kadane's algo***
        Option1: [,,,,,,,______,,,,,,] => max res
        Option2: [_______,,,,,,______] => find min in the middle

        if minSubarray is the entire array (all negative):
            return the largest num (option 1)
        """
        maxSum = minSum = nums[0]
        curMax = curMin = totalSum = 0 
        for n in nums:
            # max
            curMax += n
            maxSum = max(maxSum, curMax)
            curMax = max(0, curMax)

            # min
            curMin += n
            minSum = min(minSum, curMin)
            curMin = min(0, curMin)

            # totalSum
            totalSum += n

        if totalSum == minSum:
            return maxSum
        return max(totalSum-minSum, maxSum)