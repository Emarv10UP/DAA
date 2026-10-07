# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        a = ListNode(0, head)
        b = a
        
        while b and b.next:
            if b.next.val == val:
                b.next = b.next.next
            else:
                b = b.next
        return a.next
