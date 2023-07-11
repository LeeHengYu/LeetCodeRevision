# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k==0:
            return [target.val]
        # need to find upward so parent map is useful
        q = [root]
        parent = {}
        while q:
            cur = q.pop(0)
            if (cur.left):
                q.append(cur.left)
                parent[cur.left]=cur
            if (cur.right):
                q.append(cur.right)
                parent[cur.right]=cur
        
        q.append(target) # BFS from target
        # if the traversal hits root, it will bounce back
        visit = set()
        visit.add(target)
        dist = 0
        while q:
            n = len(q)
            for _ in range(n):
                cur = q.pop(0)
                if cur in parent and parent[cur] not in visit:
                    q.append(parent[cur])
                    visit.add(parent[cur])
                if cur.left and cur.left not in visit:
                    q.append(cur.left)
                    visit.add(cur.left)
                if cur.right and cur.right not in visit:
                    q.append(cur.right)
                    visit.add(cur.right)
            dist+=1
            if dist==k:
                break
        res = []
        while q:
            res.append(q.pop(0).val)

        return res