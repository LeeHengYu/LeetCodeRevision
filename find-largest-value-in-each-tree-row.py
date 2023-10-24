# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        q = [(root,0)]

        while q:
            node, level = q.pop(0)
            if level >= len(res):
                res.append(node.val)
            else:
                res[level] = max(res[level], node.val)
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right,level+1))
        return res