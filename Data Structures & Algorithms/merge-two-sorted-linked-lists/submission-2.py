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
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val<list2.val: 
            list1.next= self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next= self.mergeTwoLists(list1,list2.next)
            return list2
