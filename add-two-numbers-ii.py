# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1, ll2 = [], []
        while l1:
            ll1.append(l1.val)
            l1=l1.next
        while l2:
            ll2.append(l2.val)
            l2=l2.next
        while len(ll1)<len(ll2):
            ll1 = [0]+ll1
        while len(ll1)>len(ll2):
            ll2 = [0]+ll2
        # padding
        carry=0
        nxt = None
        for i in range(len(ll1)-1,-1,-1):
            v=ll1[i]+ll2[i]+carry
            val = v%10
            carry = v//10
            temp = ListNode(val)
            temp.next = nxt
            nxt = temp
        if carry:
            temp = ListNode(1)
            temp.next = nxt
            nxt=temp
        return nxt