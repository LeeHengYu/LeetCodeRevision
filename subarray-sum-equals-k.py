class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum
        prefix = {0:1}
        total = 0
        res = 0
        for n in nums:
            total += n
            res += prefix.get(total-k,0)
            prefix[total] = prefix.get(total,0)+1

        return res
    
# O(n^2) solution: TLE
# O(n) using hashmap 
# JPM interview question