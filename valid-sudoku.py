from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = defaultdict(set)
        COL = defaultdict(set)
        BLK = defaultdict(set) # block index from (0,0) to (2,2)

        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n==".":
                    continue

                if (
                    n in ROW[r] or
                    n in COL[c] or
                    n in BLK[(r//3, c//3)]
                ): return False

                ROW[r].add(n)
                COL[c].add(n)
                BLK[(r//3, c//3)].add(n)

        return True