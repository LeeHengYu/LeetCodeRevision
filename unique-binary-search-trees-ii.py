# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        def solve(left,right):
            if left>right:
                return [None]
            if left==right:
                return [TreeNode(left)]
            if (left,right) in dp:
                return dp[(left,right)]
            
            res = []
            
            for i in range(left,right+1):
                lefts = solve(left, i-1)
                rights = solve(i+1, right)
                for l in lefts:
                    for r in rights:
                        res.append(TreeNode(i,l,r))
            dp[(left,right)]=res
            return res
        return solve(1,n)