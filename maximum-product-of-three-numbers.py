# Trivial solution: sorting O(nlogn)
import statistics


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max3, max2, max1 = -1000, -1000, -1000  # big three max3<max2<max1
        min1, min2 = 1000, 1000  # small two min1<min2

        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max3*max2*max1, max1*min1*min2)