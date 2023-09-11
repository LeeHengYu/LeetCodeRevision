from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        gps = defaultdict(list)
        res = []
        for i, p in enumerate(groupSizes):
            gps[p].append(i)
            if len(gps[p])==p:
                res.append(gps[p].copy())
                gps[p] = []
        return res