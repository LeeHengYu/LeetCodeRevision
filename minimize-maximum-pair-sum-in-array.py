class Solution:
    def minPairSum(self, arr: List[int]) -> int:
        arr.sort()
        i, j = 0, len(arr)-1
        res = 0
        while i<j:
            res = max(res, arr[i]+arr[j])
            i+=1; j-=1
        return res