"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mp = {}
        if not node: return None

        def clone(node):
            if not node:
                return None
            if node in mp:
                return mp[node]
            
            copy = Node(node.val)
            mp[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei)) # Recursion 
            return copy

        return clone(node)