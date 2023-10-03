from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ct = Counter(nums)
        return sum([n*(n-1)//2 for n in ct.values() if n>=2])