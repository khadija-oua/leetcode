# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head 
        while curr : 
            size +=1
            curr = curr.next
        m = size - n 
        if size == 0 or size ==1 :
            head = None 
            return head 
        curr = head
        l= 0
        while curr : 
            l+=1
            if m == 0 : 
                return head.next
            if l == m :
                if curr.next and curr.next.next :
                    curr.next = curr.next.next
                    break
                else :
                    curr.next = None
            curr = curr.next
        return head
        