class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [] # non-increasing queue
        res = []
        for i in range(len(nums)):
            if q and q[0]<=i-k:
                q.pop(0) # out of range
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
            if i>=k-1:
                res.append(nums[q[0]])
        return res