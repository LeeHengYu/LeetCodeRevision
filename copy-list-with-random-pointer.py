copy-list-with-random-pointer"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        map = {}
        cur = head
        while cur:
            map[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.next: map[cur].next = map[cur.next]
            if cur.random: map[cur].random = map[cur.random]
            cur = cur.next
        return map[head]