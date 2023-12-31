class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count = defaultdict(list)
        for i, c in enumerate(s):
            count[c].append(i)
        
        res = -1
        for ls in count.values():
            res = max(res, ls[-1] - ls[0] - 1)
        return res