import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # heaps
        left = []
        right = []
        n = len(costs)
        for i in range(candidates):
            if costs:
                heapq.heappush(left, costs[0])
                costs.pop(0)
            if costs:
                heapq.heappush(right, costs[-1])
                costs.pop()

        res = 0
        for i in range(k):
            if not right or (left and left[0] <= right[0]):
                res += heapq.heappop(left)
                if costs:
                    heapq.heappush(left, costs[0])
                    costs.pop(0)
            else:
                res += heapq.heappop(right)
                if costs:
                    heapq.heappush(right, costs[-1])
                    costs.pop()
        return res
