# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = []
        q.append(root)

        level = 1
        while q:
            N = len(q)
            for i in range(N):
                temp = q.pop(0)
                if not (temp.left or temp.right):
                    return level
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            level += 1

        return level