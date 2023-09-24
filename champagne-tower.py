class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row = [poured]
        for row in range(1,query_row+1):
            cur = [0]*(row+1) 
            for i in range(row):
                extra = prev_row[i] - 1
                if extra > 0:
                    cur[i] += extra*0.5
                    cur[i+1] += extra*0.5
            prev_row = cur
        return min(1, prev_row[query_glass])