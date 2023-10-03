class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # flatten the board is good
        ROW = len(board)
        dest = ROW*len(board[0])
        newBoard = [0] # flattened board
        temp = 0
        for i in range(ROW-1, -1, -1):
            if temp%2: # need reversing
                newBoard.extend(reversed(board[i]))
            else:
                newBoard.extend(board[i])
            temp += 1

        # BFS
        q = [1] # FIFO
        dist = 0
        visit = {1} # if enter q, add to visit
        while q:
            N = len(q)
            for _ in range(N):
                node = q.pop(0)
                if node==dest: return dist 
                for nei in range(node+1, min(dest, node+6)+1):
                    if newBoard[nei] != -1:
                        nei = newBoard[nei] # snake or ladder

                    if nei in visit: continue
                    q.append(nei)
                    visit.add(nei)

            dist += 1
        return -1