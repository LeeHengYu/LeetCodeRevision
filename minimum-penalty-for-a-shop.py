class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        Y, N = customers.count('Y'), 0
        min_pen = Y+N
        res = 0
        for i, c in enumerate(customers):
            if c =='Y':
                Y-=1
            elif c=='N':
                N+=1
            if Y+N < min_pen:
                min_pen = Y+N
                res = i+1
        return res