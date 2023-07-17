# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, bar):
            nonlocal res
            if not node:
                return
            if node.val>=bar:
                res += 1
            dfs(node.left, max(node.val, bar))
            dfs(node.right, max(node.val, bar))

        
        dfs(root, -10001)
        return res