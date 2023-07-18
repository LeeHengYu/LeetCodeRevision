# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev 