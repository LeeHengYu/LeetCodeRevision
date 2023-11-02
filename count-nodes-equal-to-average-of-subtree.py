# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        @cache
        def help(node):  # [sum, size]
            nonlocal res
            if not node: return [0, 0]
            sumL, sizeL = help(node.left)
            sumR, sizeR = help(node.right)
            tempSum = sumL+sumR+node.val
            tempSize = sizeL + sizeR + 1
            if node.val == tempSum//tempSize:
                res += 1
            return [tempSum, tempSize]
        
        help(root)
        return res