class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        for i in range(1, len(colors)):
            if colors[i-1] == colors[i]:
                if neededTime[i-1] < neededTime[i]:
                    res += neededTime[i-1]
                else:
                    res += neededTime[i]
                    neededTime[i] = neededTime[i-1]
        return res