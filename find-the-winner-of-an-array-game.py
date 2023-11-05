class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i, j = 0, 1
        streak = 0

        while streak != k:
            if j >= len(arr) or i >= len(arr):
                return arr[i] # return the largest

            if arr[i] > arr[j]:
                streak += 1
            else:
                streak = 1
                i = j

            j += 1
        return arr[i]