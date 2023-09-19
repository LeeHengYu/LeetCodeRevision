class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=fast=0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast: break
        fast = 0
        while 1: 
            fast = nums[fast]
            slow = nums[slow]
            if slow==fast: return slow