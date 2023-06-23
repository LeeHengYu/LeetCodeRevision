class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return 2

        res = 2
        cache = defaultdict(dict)
        # { idx: { diff: count, ... } }

        for i in range(1, n):
            for j in range(i):
                diff = nums[i]-nums[j]
                cache[i][diff] = cache[j].get(diff, 1)+1
                res = max(res, cache[i][diff])

        return res
        # O(n^2)
