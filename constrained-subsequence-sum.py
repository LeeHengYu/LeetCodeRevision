class Solution:
    def constrainedSubsetSum(self, A: List[int], k: int) -> int:
        dp = A.copy() # max number: only itself
        q = [(-A[0],0)] # max heap
        for i in range(1,len(A)): 
            while q[0][1]<i-k: # evict out-of-bound dp elements
                heappop(q)
            dp[i] = max(dp[i], A[i]-q[0][0]) # consider taking the largest in the heap 
            heappush(q, (-dp[i],i)) # push the max num accumulated so far
        return max(dp)