# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = ListNode()
        
        p_result = result_list
        p_list1  = list1
        p_list2  = list2
        
        while p_list1 and p_list2:
            if p_list1.val < p_list2.val:
                p_result.next = ListNode(p_list1.val)
                p_list1       = p_list1.next
            else:
                p_result.next = ListNode(p_list2.val)
                p_list2       = p_list2.next
            p_result = p_result.next
                
        p_list = p_list1 if p_list1 else p_list2
        while p_list:
            p_result.next = ListNode(p_list.val)
            p_list        = p_list.next
            p_result = p_result.next
            
        return result_list.next
        