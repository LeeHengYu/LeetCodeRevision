class Solution: # O(n)
    def maxProductDifference(self, nums: List[int]) -> int:
        s1, s2, l2, l1 = sorted(nums[:4])
        for i in range(4, len(nums)):
            if s2 <= nums[i] <=l2:
                continue
            elif l2 < nums[i] < l1:
                l2 = nums[i]
            elif nums[i] >= l1:
                l2, l1 = l1, nums[i]
            elif s1 < nums[i] < s2:
                s2 = nums[i]
            else:
                s2, s1 = s1, nums[i]
        return (l1*l2)-(s1*s2)
    
class Solution: # O(nlogn)
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]*nums[-2])-(nums[0]*nums[1])