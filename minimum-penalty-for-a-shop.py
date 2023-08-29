class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        Y, N = customers.count('Y'), 0
        min_pen = temp = Y+N
        res = 0
        for i, c in enumerate(customers):
            temp += (1 if c=='N' else -1)
            if temp < min_pen:
                min_pen = temp
                res = i+1
        return res