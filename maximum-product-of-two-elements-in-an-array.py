class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        # method 1: brute force
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                res = max(res, (nums[i]-1)*(nums[j]-1))
        return res

class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        # method 2: max heap
        pq = [-nums[0]] # max heap
        res = 0
        for i in range(1,len(nums)):
            temp = (nums[i]-1)*(-pq[0]-1)
            res = max(res, temp)
            heappush(pq, -nums[i])
        return res