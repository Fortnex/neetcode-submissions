# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None)
        val1 = ''
        while l1: 
            val1+=str(l1.val)
            l1 = l1.next
        val1= int(val1[::-1])
        val2 = ''
        while l2: 
            val2+=str(l2.val)
            l2 = l2.next
        val2 = int(val2[::-1])
        val3 = int(str(val1+val2))
        head = ListNode(val3%10)
        cur = head
        val3=val3//10
        while val3: 
            head.next = ListNode(val3%10)
            val3 = val3//10
            head = head.next
        return cur

