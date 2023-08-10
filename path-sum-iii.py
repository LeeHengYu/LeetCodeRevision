# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], tgt: int) -> int:
        if not root: return 0
        prefix = defaultdict(int)
        prefix[0]=1
        res = 0
        def dfs(node, total):
            nonlocal res
            if not node: 
                return
            total+=node.val
            if total - tgt in prefix: # total - a prefixSum = tgt
                res+=prefix[total - tgt]
            prefix[total]+=1
            dfs(node.left, total)
            dfs(node.right, total)
            prefix[total]-=1 # backtrack
        dfs(root, 0)
        return res