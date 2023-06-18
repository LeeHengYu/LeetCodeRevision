class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if letters[mid] > target and (mid == 0 or letters[mid-1] <= target):
                return letters[mid]
            elif letters[mid] <= target:
                l = mid+1
            else:
                r = mid-1
        return letters[0]
