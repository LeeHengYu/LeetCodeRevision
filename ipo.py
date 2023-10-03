from heapq import heappop, heappush

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        sort by capital requirements
        in each selection:
        push all available projects into maxHeap
        all available projects will still become available in the next round
        """
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort()
        
        maxHeap = []
        for _ in range(k):
            while projects and w >= projects[0][0]:
                __, profit = projects.pop(0)
                heappush(maxHeap, -profit)
            
            if not maxHeap:
                break
            w -= heappop(maxHeap)

        return w