class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res = 0
        for x in left:
            res = max(res, x)
        for x in right:
            res = max(res, n-x)

        return res