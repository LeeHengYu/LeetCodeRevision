# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        n = 0
        while cur:
            n+=1
            cur = cur.next
        quo, rem = n//k, n%k
        res = []
        cur = head
        for i in range(k):
            partialHead = cur
            # need to handle the last node of each partition
            # no of nodes: 
            # if i<rem: quo+1, else: quo
            for j in range(quo+(i<rem)-1):
                if cur:
                    cur = cur.next
            if cur:
                temp = cur.next
                cur.next = None
                cur = temp
            res.append(partialHead)
            
        return res