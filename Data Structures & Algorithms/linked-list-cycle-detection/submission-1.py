# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vals = []
        c = 0 

        while head and not c: 
            if head.val in vals: 

                c = 1

            vals.append(head.val)
            
            head=head.next

        if c==1 and not head:
            
            return False
        if not head: 
            return False
        else:
            return True