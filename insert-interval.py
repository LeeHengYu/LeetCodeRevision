class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
                #finish processing, return directly

            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) #still scanning

            else:
                newInterval[0] = min(intervals[i][0],newInterval[0])
                newInterval[1] = max(intervals[i][1],newInterval[1])
            #if there is any overlapping, merging intervals by keeping track of the lower and upper bound

        res.append(newInterval)
        return res
            