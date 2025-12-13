# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        curr= head 
        while curr :
            len+=1
            curr= curr.next 
        mid = len //2
        N=ListNode(0)
        N=head
        for i in range(mid):
            N = N.next
        return N
