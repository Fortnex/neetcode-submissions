# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
3 scenarios: 
1 is less than 2 and 1 points to 2
2 is less than 1 and 2 points to 1 
1 is lesser than 2nd of 2 so it just keeps going


"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dum = ListNode()
        node = dum
        curr1=  list1
        curr2=list2

        while curr1 and curr2: 
            if curr1.val<curr2.val: 
                node.next = curr1
                curr1=curr1.next
            else: 
                node.next = curr2
                curr2= curr2.next
            node = node.next
        node.next = curr1 or curr2

        return dum.next