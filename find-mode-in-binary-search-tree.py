# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        tra = []
        
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            tra.append(node.val)
            inorder(node.right)

        inorder(root)

        ct = Counter(tra)
        maxCt = max(ct.values())
        return [x for x in ct if ct[x]==maxCt]