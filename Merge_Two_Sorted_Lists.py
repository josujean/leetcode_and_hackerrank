# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = ListNode()
        pointer = merged

        while l1 and l2:
            if l1.val > l2.val:
                pointer.next = l2
                l2 = l2.next
            else:
                pointer.next = l1
                l1 = l1.next
            pointer = pointer.next
        
        if l1 == None:
            pointer.next = l2
        if l2 == None:
            pointer.next = l1

        return merged.next
