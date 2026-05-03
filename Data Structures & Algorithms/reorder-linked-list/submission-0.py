# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fuck ass i looked at the solution

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        sh  = slow.next

        slow.next= None
        #joining part comes here

        #reversing part 
        prev,curr  = None,sh
        
        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        sh = prev

        start = head
        while sh and start: 
            temp = start.next 
            temp2 = sh.next
            start.next = sh 
            sh.next=  temp
            start = temp
            sh = temp2
        
        



        












