# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head 
        while tail:
            if tail.next and tail.val == tail.next.val :
                if tail.next.next :
                    tail.next = tail.next.next
                else : tail.next = None

            tail = tail.next
        return head