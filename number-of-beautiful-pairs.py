class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                first = int(str(nums[i])[0])
                last = nums[j] % 10
                if gcd(first, last) == 1:
                    res += 1
        return res
