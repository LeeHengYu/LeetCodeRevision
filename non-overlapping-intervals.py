class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        n = len(intervals)
        ans = 0
        rightbound = intervals[0][1]
        for i in range(n-1):
            if intervals[i+1][0]<rightbound: #overlapping
                ans += 1
            else:
                rightbound = intervals[i+1][1] #update right bound

        return ans