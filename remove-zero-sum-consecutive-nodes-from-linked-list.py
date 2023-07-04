# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Hint: From test case 3, use stack.
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prefix = {0: dummy}
        stack = []
        total = 0
        while head:
            total += head.val

            if total in prefix:
                while stack and stack[-1]!=total:
                    temp = stack.pop()
                    prefix.pop(temp)
            # guarantee no duplicates of prefix sums
            else:
                prefix[total]=head
                stack.append(total)

            head = head.next

        cur = dummy
        last = 0
        while stack:
            curval = stack.pop(0)
            cur.next = ListNode(curval - last)
            cur = cur.next
            last = curval

        return dummy.next