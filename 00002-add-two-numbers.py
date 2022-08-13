# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        p      = result

        carry = 0
        while l1 or l2:
            a  = l1.val  if l1 else 0
            b  = l2.val  if l2 else 0
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            sum = a + b + carry
            carry = int(sum / 10)
            
            p.next = ListNode(sum % 10)
            p      = p.next
        
        if carry != 0:
            p.next = ListNode(carry)
            p      = p.next
        
            
        return result.next
        