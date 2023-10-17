class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indeg = [0]*n 
        for i in range(n):
            if leftChild[i]!=-1:
                indeg[leftChild[i]]+=1
            if rightChild[i]!=-1:
                indeg[rightChild[i]]+=1

        head = -1
        for i in range(n):
            if indeg[i] == 0:
                if head==-1:
                    head = i
                else:
                    return False # more than one possible root
        if head == -1:
            return False # no root
        
        visit = [False]*n
        q = [head] # FIFO DS
        while q:
            cur = q.pop(0)
            if visit[cur]:
                return False
            visit[cur] = True 
            if leftChild[cur]!=-1:
                q.append(leftChild[cur])
            if rightChild[cur]!=-1:
                q.append(rightChild[cur])
        return sum(visit) == n 