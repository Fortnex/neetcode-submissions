# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        l = 0

        while cur: 
            l+=1
            cur=cur.next
        p = l-n
        i=0
        cur= head 
        if l==1: 
            return None
            
        if n==l:
            head=  head.next
            
        else:
            while i<p-1:

                i+=1
                cur= cur.next
            cur.next=  cur.next.next

        return head