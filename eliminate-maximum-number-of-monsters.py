class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [d/s for d,s in zip(dist,speed)]
        time.sort(reverse=True)
        res = 0
        t = 0
        i = len(time) - 1
        while i>=0 and time[i]>t:
            res += 1
            i -= 1
            t += 1
        return res 