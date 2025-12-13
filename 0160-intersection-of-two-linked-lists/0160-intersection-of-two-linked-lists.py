# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB
        while A != B :
            if A is None: A=headB
            else :  A=A.next 
            if B is None: B=headA
            else :  B= B.next
           
        return A

        