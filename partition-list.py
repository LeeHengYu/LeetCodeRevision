# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sHead = sCur = ListNode(-1)
        lHead = lCur = ListNode(-1)
        while head:
            if head.val<x:
                sCur.next = head
                sCur = sCur.next
            else:
                lCur.next = head
                lCur = lCur.next
            head = head.next
        lCur.next = None
        sCur.next = lHead.next
        return sHead.next