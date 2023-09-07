# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1: # recursion
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            return reverse(nxt, cur)
        return reverse(head,None)

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = None, dummy.next
        while cur:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        dummy.next = prev
        return dummy.next