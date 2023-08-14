from heapq import heapify, heappop, heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minH = nums[:k]
        heapify(minH)
        for n in nums[k:]:
            if n>minH[0]:
                heappop(minH)
                heappush(minH, n)
        return minH[0]