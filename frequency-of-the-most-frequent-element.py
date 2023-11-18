class Solution:
    def maxFrequency(self, arr: List[int], k: int) -> int:
        arr.sort()
        # Sliding Window
        l = r = 0
        res = tempSum = 0
        while r < len(arr):
            tempSum += arr[r]
            while arr[r]*(r-l+1) > tempSum + k:
                tempSum -= arr[l]
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res 