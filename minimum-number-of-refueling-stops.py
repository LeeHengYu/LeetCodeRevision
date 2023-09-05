from heapq import heappush, heappop
class Solution:
    def minRefuelStops(self, target: int, tank: int, stations: List[List[int]]) -> int:
        if tank>=target: return 0
        # rename startFuel => tank
        maxH = []
        prev = 0
        res = 0
        # suppose there is a gas station at target, the goal is to reach this gas station
        stations.append([target, 0])
        n = len(stations)
        for i in range(n):
            pos, supply = stations[i]
            tank -= (pos - prev)
            while tank<0:
        # unable to reach ith station, refuel at previous stations that supplies the most fuel (greedy)
                if not maxH: return -1
                tank -= heappop(maxH)
                res += 1
            if tank+pos>=target: return res # enough to reach target
            heappush(maxH, -supply)
            prev = pos
        return -1