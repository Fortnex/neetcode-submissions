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

        while list1!=None and list2!=None: 
            if list1.val<list2.val: 
                node.next = list1
                list1 = list1.next
            else: 
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        dum = dum.next
        
        return dum
        
