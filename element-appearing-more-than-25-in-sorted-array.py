from bisect import bisect_left, bisect_right
from collections import Counter

class Solution1:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n-1
        # check 3 numbers
        # 25%, 50%, 75%
        for num in (arr[n//4], arr[n//2], arr[3*n//4]):
            length = bisect_right(arr, num) - bisect_left(arr, num)
            if length > n/4:
                return num
        return -1

class Solution2:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        ct = Counter(arr)
        for num in ct:
            if ct[num]>n/4:
                return num