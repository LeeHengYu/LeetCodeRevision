class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # look for 2, 3, 1 pattern from the back
        stack = [] # decreasing
        k = -inf # mid num
        for num in reversed(nums):
            if num<k: return True # check nums[i]<nums[k]
            while stack and stack[-1]<num:
                k = stack.pop()
                # best possible nums[k], here already guarantee nums[j]>nums[k]
            stack.append(num) 
        return False