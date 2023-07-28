from collections import defaultdict
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        prefix = []
        total=0
        for n in nums:
            total+=n
            prefix.append(total)
        def partialsum(i,j):
            return prefix[j]-(prefix[i-1] if i>=1 else 0)
        
        dp = defaultdict(int)
        def solve(i,j):
            if i==j:
                return nums[i]
            if (i,j) in dp:
                return dp[(i,j)]

            pickFirst = nums[i] + partialsum(i+1,j) - solve(i+1,j)
            pickLast = nums[j] + partialsum(i,j-1) - solve(i,j-1)
            res = max(pickFirst, pickLast)
            dp[(i,j)] = res
            return res
        return solve(0,len(nums)-1)>=prefix[-1]/2