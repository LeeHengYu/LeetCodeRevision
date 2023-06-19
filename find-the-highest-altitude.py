class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        res = 0
        cumsum = 0
        for n in gain:
            cumsum += n
            res = max(res, cumsum)
        return res
