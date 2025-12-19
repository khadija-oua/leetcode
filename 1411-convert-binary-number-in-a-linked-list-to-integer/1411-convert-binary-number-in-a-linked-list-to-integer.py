# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr = head 
        n=-1
        while curr:
            n+=1
            curr= curr.next
        S=0
        if n==-1 : return 0
        curr = head
        while curr:
            S+=(curr.val)*(2**n)
            curr = curr.next
            n-=1
        return S



