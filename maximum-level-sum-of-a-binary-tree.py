# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf"), 0]
        level = 1
        q = []
        q.append(root)
        while q:
            N = len(q)
            temp = 0
            for i in range(N):
                cur = q.pop(0)
                temp += cur.val
                if (cur.left):
                    q.append(cur.left)
                if (cur.right):
                    q.append(cur.right)
            if (res[0] < temp):
                res = [temp, level]
            level += 1

        return res[1]
