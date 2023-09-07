# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right: return head
        dummy = ListNode(0, head)
        leftPrev = dummy
        for _ in range(left-1):
            leftPrev = leftPrev.next
        # step one done
        prev, cur = None, leftPrev.next
        for j in range(right-left+1):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        # step two done

        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next