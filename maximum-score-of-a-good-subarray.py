class Solution:
    def maximumScore(self, A: List[int], k: int) -> int:
        l = r = k
        curMin = res = A[k]

        while l>0 or r<len(A)-1:
            if l==0 or (r+1<len(A) and A[r+1]>A[l-1]):
                r += 1
            else:
                l -= 1
            curMin = min(curMin, A[l], A[r])
            res = max(res, curMin*(r-l+1))

        return res