# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA, listB = headA, headB

        while listA != listB:
            if listA is not None:
                listA = listA.next
            else:
                listA=headB
            if listB is not None:
                listB = listB.next
            else:
                listB = headA
        return listA
        
