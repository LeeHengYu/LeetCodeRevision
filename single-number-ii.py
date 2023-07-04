class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(n)/O(1) solution: bit manipulation
        # More Friendly solution: hashmap O(2n)/O(n)
        count = {}
        for n in nums:
            count[n] = count.get(n,0)+1
        for i, ct in count.items():
            if ct==1:
                return i
        # Bit manipulation solution
        # https://leetcode.com/problems/single-number-ii/solutions/2761958/python3-bit-manipulation/
        # As I think it is not really possible to think of this solution in an interview,
        # I chose to reference a solution in the discussion and only keep the hashmap solution. 