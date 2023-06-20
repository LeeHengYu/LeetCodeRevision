class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # CumSum
        n = len(nums)
        if n < 2*k+1:
            return [-1]*n
        cumsum = []
        temp = 0
        for val in nums:
            temp += val
            cumsum.append(temp)

        res = []
        deno = 2*k+1
        for i in range(n):
            if i+k >= n or i-k < 0:
                res.append(-1)  # out of bound
            else:
                if i == k:
                    val = cumsum[i+k]
                else:
                    val = cumsum[i+k]-cumsum[i-k-1]
                res.append(val//(2*k+1))
        return res
