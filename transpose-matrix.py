import numpy as np
class Solution1:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        res = []
        for col in range(c):
            temp = [ matrix[row][col] for row in range(r) ]
            res.append(temp)
        return res
    
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return np.array(matrix).transpose().tolist()