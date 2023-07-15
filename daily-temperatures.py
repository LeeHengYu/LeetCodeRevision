class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # decreasing monotonic stack, (temp, idx)
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
                t, idx = stack.pop()
                res[idx] = i-idx
            stack.append((temp, i))
        return res