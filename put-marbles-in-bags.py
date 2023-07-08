class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k==1 or k==len(weights):
            return 0

        costs = [weights[i]+weights[i+1] for i in range(len(weights)-1)]
        costs.sort()
        res_min = sum(costs[:k-1])
        costs.reverse()
        res_max = sum(costs[:k-1])
        return res_max-res_min



    # https://leetcode.com/problems/put-marbles-in-bags/solutions/3111583/python3-sort-the-separators-o-n-log-n-2-lines/