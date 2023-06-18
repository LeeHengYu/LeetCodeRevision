# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        res = [-200000, 100001]  # last node, final ans

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res[1] = min(res[1], node.val-res[0])
            res[0] = node.val
            inorder(node.right)

        inorder(root)
        return res[1]
