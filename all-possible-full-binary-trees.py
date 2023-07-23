from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        dp = defaultdict(list)
        dp[1] = [TreeNode()]
        def help(k):   
            if k%2==0 or k<1: return []
            if k in dp:
                return dp[k]

            res = []
            for i in range(1,k,2):
                for left in help(i):
                    for right in help(k-i-1): 
                        res.append(TreeNode(0,left,right))

            dp[k] = res
            return res
                
        return help(n)