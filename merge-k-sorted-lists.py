# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # maintain a PQ
        minH = []
        n = len(lists)
        for i in range(n):
            if lists[i]:
                heappush(minH, (lists[i].val, i)) # (val, index)
                lists[i] = lists[i].next

        dummyHead= ListNode()
        cur = dummyHead
        while minH:
            val, idx = heappop(minH)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[idx]:
                heappush(minH, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummyHead.next