# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop, heappush

class Solution1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # pq method
        pq = []
        n = len(lists)
        dummy = cur = ListNode()
        for i in range(n):
            if lists[i]:
                heappush(pq, [lists[i].val, i])
                lists[i] = lists[i].next
        while pq:
            val, idx = heappop(pq)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[idx]:
                heappush(pq, [lists[idx].val, idx])
                lists[idx] = lists[idx].next
        return dummy.next
    
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        while len(lists)>1:
            mergeLists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else None
                mergeLists.append(self.mergeTwo(l1, l2))
            lists = mergeLists
        return lists[0]

    def mergeTwo(self, l1, l2):
        dummy = cur = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next