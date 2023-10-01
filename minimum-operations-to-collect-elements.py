class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        count = 0
        for n in reversed(nums):
            count += 1
            if n>k: continue
            seen.add(n)
            
            if len(seen)==k:
                return count 
        return -1